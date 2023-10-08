from sqlalchemy import *

class DBUtils:
    # Database access constants for mysql connections (Sensitive data hidden)

    database_server = '127.0.0.1'
    database_port = 3306  # 3306
    database_name = 'lte'
    database_username = 'root'
    database_password = 'root'

def get_db_connection():
    # Create SQLAlchemy engine and connection
    engine = create_engine ("mysql://{0}:{1}@{2}:{3}/{4}".format(
                                    DBUtils.database_username,
                                    DBUtils.database_password,
                                    DBUtils.database_server,
                                    DBUtils.database_port,
                                    DBUtils.database_name), encoding="utf-8")
    conn = engine.connect()
    return conn
