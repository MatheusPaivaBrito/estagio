from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

username = "root"
password = "root"
db_name = "fastapi"

DATABASE_URL = 'mysql+pymysql://' + username + ':' + password + '@localhost:3306/' + db_name
engine = create_engine(DATABASE_URL)

Base = declarative_base()
