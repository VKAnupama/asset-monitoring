from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "asm_db"
DB_USER = "asm_user"
DB_PASSWORD = "asmuser"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

# IMPORTANT: Base class for all models
Base = declarative_base()



