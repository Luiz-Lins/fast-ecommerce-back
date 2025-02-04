from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'FAST Ecommerce API'
    items_per_user: int = 50

    class Config:
        env_file = '.env'
