import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv("customer_shopping_behavior.csv")


# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:YOURPASSWORD@localhost/customer_analytics"
)

# Upload DataFrame to MySQL
df.to_sql(
    name="customer_shopping",   # Table name in MySQL
    con=engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully!")