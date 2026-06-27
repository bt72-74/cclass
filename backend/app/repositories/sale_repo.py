from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
from app.models.sale import Sale
from app.models.sale_item import SaleItem
from app.schemas.sale import SaleCreate


def generate_invoice_number(db: Session) -> str:
    today_str = datetime.today().strftime("%Y%m%d")
    count_today = db.query(func.count(Sale.id))\
        .filter(func.date(Sale.invoice_date) == datetime.today().date())\
        .scalar() or 0
    return f"INV-{today_str}-{count_today + 1:04d}"


def create_sale(db: Session, sale_in: SaleCreate) -> Sale:
    invoice_number = generate_invoice_number(db)

    sale = Sale(
        invoice_number=invoice_number,
        customer_id=sale_in.customer_id,
        salesperson_id=sale_in.salesperson_id,
        invoice_date=sale_in.invoice_date or datetime.utcnow(),
    )
    db.add(sale)
    db.flush()  # تا id داشته باشیم

    total_amount = 0
    total_cost = 0

    for item_in in sale_in.items:
        line_amount = item_in.quantity * item_in.unit_price
        line_cost = item_in.quantity * item_in.cost_price
        line_profit = line_amount - line_cost

        item = SaleItem(
            sale_id=sale.id,
            product_id=item_in.product_id,
            quantity=item_in.quantity,
            unit_price=item_in.unit_price,
            cost_price=item_in.cost_price,
            line_amount=line_amount,
            line_profit=line_profit
        )
        db.add(item)

        total_amount += line_amount
        total_cost += line_cost

    sale.total_amount = total_amount
    sale.total_cost = total_cost
    sale.total_profit = total_amount - total_cost

    db.commit()
    db.refresh(sale)
    return sale


def get_sale_by_id(db: Session, sale_id: int) -> Sale | None:
    return db.query(Sale).filter(Sale.id == sale_id).first()


def list_sales(db: Session, skip=0, limit=50):
    return db.query(Sale).order_by(Sale.invoice_date.desc()).offset(skip).limit(limit).all()


def delete_sale(db: Session, sale: Sale):
    db.delete(sale)
    db.commit()
