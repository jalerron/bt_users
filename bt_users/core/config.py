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
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 50
    pool_size: int = 10
    # str = f'postgresql://postgres:PosSwtbme6^98(*@localhost/users_app'

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig

    # database_url: str = f'postgresql://postgres:PosSwtbme6^98(*@localhost/users_app'

settings = Settings(
    _env_file = ('.env.template', '.env'),
    _env_file_encoding = 'utf-8',
    )   