import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/cleaned_orders_data.csv")

username = "kim"
host = "localhost"
port = "5432"
database = "orders_analytics"

engine = create_engine(
    f"postgresql+psycopg2://{username}@{host}:{port}/{database}"

)

df.to_sql(
    "orders",
    engine,
    if_exists="replace",
    index=False
)

print("Cleaned data loaded into PostgreSQL.")