from click.core import F
from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


# DB_VALUES
# DB_USERNAME = get_key('.env','DB_USERNAME')
# DB_USERPASS = get_key('.env','DB_USERPASS')
# DB_NAME = get_key('.env','DB_NAME')

class RunConfig(BaseModel):
    server_host: str = '127.0.0.1'
    server_port: int = 8000

class ApiPrefix(BaseModel):
    prefix: str = '/api'


class DatabaseConfig(BaseModel):
    # Define URL field that will be overridden by environment variables
    url: PostgresDsn = f"postgresql+asyncpg://user:password@localhost/base"
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
        # Remove APP_CONFIG__ prefix to simplify env variable names
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()

settings = Settings(
    _env_file=("bt_users/.env.template","bt_users/.env"),
    _env_file_encoding="utf-8",
)
print(settings.db.url)
# Now you can set DB_URL in .env file like:
# DB__URL=postgresql+asyncpg://username:password@localhost/dbname
