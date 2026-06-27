from pydantic_settings import BaseSettings
 
 
class Settings(BaseSettings):
    PROJECT_NAME: str = "Stationery BI Platform"
    API_V1_STR: str = "/api/v1"
 
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "stationery_bi"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
 
    JWT_SECRET_KEY: str = "super-secret-key-change-me"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
 
    REDIS_URL: str = "redis://localhost:6379/0"
 
    GEMINI_API_KEY: str = ""
 
    model_config = {"env_file": ".env", "extra": "ignore"}
 
 
settings = Settings()