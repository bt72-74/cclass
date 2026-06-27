from app.core.database import engine, Base
import app.models
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.routes import auth


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)
    Base.metadata.create_all(bind=engine)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://localhost:3001",
            "http://127.0.0.1:3000",
            "http://127.0.0.1:3001",
            "https://localhost:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router, prefix=settings.API_V1_STR)
    
    return app


app = create_app()
from app.api.v1.routes import dashboard

app.include_router(dashboard.router, prefix=settings.API_V1_STR)
from app.api.v1.routes import products

app.include_router(products.router, prefix=settings.API_V1_STR)
from app.api.v1.routes import sales

app.include_router(sales.router, prefix=settings.API_V1_STR)
from app.api.v1.routes import customers

app.include_router(customers.router, prefix=settings.API_V1_STR)
from app.api.v1.routes import salespersons

app.include_router(salespersons.router, prefix=settings.API_V1_STR)
from app.api.v1.routes import categories, brands

app.include_router(categories.router, prefix=settings.API_V1_STR)
app.include_router(brands.router, prefix=settings.API_V1_STR)
from app.api.v1.routes import copilot

app.include_router(copilot.router, prefix=settings.API_V1_STR)
