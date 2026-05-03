import pandas as pd

#Read raw data from CSV
df = pd.read_csv("data/Online_orders_raw_dataset.csv")

#Clean column names
df.columns = df.columns.str.strip().str.lower() #remove spaces and make lowercase

#Clean customer names
df["customer_name"] = (
    df["customer_name"]
    .astype(str) #convert into string
    .str.strip()
    .str.replace(r"\s+", " ", regex=True) #r"\s+"=find one or more spaces, reaplce with 1 space
    .str.title()

)