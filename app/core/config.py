try:
    from pydantic_settings import BaseSettings

    class Settings(BaseSettings):
        DATABASE_URL: str = "sqlite:///./crm.db"
        DEBUG: bool = True

        class Config:
            env_file = ".env"

    settings = Settings()
except Exception:
    # Fallback if pydantic-settings is not installed (keeps tests/simple runs working)
    import os

    class Settings:
        DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./crm.db")
        DEBUG: bool = os.getenv("DEBUG", "true").lower() in ("1", "true", "yes")

    settings = Settings()
