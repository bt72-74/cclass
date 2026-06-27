CREATE INDEX idx_sales_invoice_date ON sales (invoice_date);
CREATE INDEX idx_sales_customer ON sales (customer_id);
CREATE INDEX idx_sales_salesperson ON sales (salesperson_id);

CREATE INDEX idx_sale_items_product ON sale_items (product_id);
CREATE INDEX idx_products_category ON products (category_id);
CREATE INDEX idx_products_brand ON products (brand_id);
