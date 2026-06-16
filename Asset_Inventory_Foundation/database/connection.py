from sqlalchemy import create_engine

from database.postgres import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("Database connection successful")
    connection.close()
except Exception as e:
    print("Connection failed")
    print(e)

#from sqlalchemy import create_engine
#
#from database.postgres import (
 #   DB_HOST,
 #   DB_PORT,
  #  DB_NAME,
   # DB_USER
#)
#
#DATABASE_URL = (
 #   f"postgresql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#)
#
#try:
 #   engine = create_engine(DATABASE_URL)
#
 #   connection = engine.connect()
#
 #   print("Database configuration ready")
  #  print(f"Connected to: {DB_NAME}")
#
 #   connection.close()
#
#except Exception as e:
 #   print("Connection failed")
  #  print(e)
