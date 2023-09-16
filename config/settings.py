from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  app_name: str = "Mi FastAPI Backend"
  debug: bool = False
  database_url: str = ''
  secret_key: str = ''
  # Otras configuraciones, como credenciales de API, tokens, etc.

  class Config:
    env_file = ".env"  # Puedes usar un archivo .env para cargar configuraciones desde variables de entorno

# Crear una instancia de la clase Settings
settings = Settings()
