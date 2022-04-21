from sqlalchemy import create_engine
import creds

def connect_to_db():
    host = creds.host
    password = creds.password
    port = creds.port
    user = creds.user
    database = creds.database
    api_type = creds.api_type
    engine = create_engine(f'postgresql+{api_type}://{user}:{password}@{host}:{port}/{database}')
    engine.connect()
    return engine

connect_to_db()
