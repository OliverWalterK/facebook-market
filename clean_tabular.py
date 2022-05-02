from sqlalchemy import create_engine, inspect
import creds
import pandas as pd


host = creds.host
password = creds.password
port = creds.port
user = creds.user
database = creds.database
api_type = creds.api_type
engine = create_engine(f'postgresql+{api_type}://{user}:{password}@{host}:{port}/{database}')
engine.connect()


df = pd.read_sql_table('products', engine)
print(len(df))
print(df.head(100))

# The main idea is to have everything with numbers, since ML models can't parse characters or strings. So the main idea is first to convert everything that you think you need to numbers
# For example, the price can't include the $ sign, so you need to remove that from eachentry and then convert the number into a float or integer
# Also, categories need to be transformed into numbers as well. If you have, say, 3 categories (Chairs, tables, desks), you can to assign each category to a number)