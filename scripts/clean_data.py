import pandas as pd

#Read raw data from CSV
df = pd.read_csv("data/Online_orders_raw_dataset.csv")

#Clean column names
df.columns = df.columns.str.strip().str.lower() #remove spaces in the beginning and the end

#Clean customer names
df["customer_name"] = (
    df["customer_name"]
    .astype(str) #convert into string
    .str.strip()
    .str.replace(r"\s+", " ", regex=True) #r"\s+"=find one or more spaces, reaplce with 1 space
    .str.title() #capitalize the first letter

)


df["country"] = (
    df["country"]
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)

)

country_mapping = {
    "sweden": "Sweden",
    "SWEDEN": "Sweden",
    "SE": "SWEDEN",
    "finland": "Finland",
    "FI": "Finland",
    "portugal": "Portugal",
    "PORTUGAL": "Portugal",
    "france": "France",
    "FRANCE": "France",
    "switzerland": "Switzerland",
    "US": "United States",
    "usa": "United States",
    "United states": "United States",
    "united states": "United States"

}

df["country"] = df["country"].replace(country_mapping)
df["country"] = df["country"].str.title()

#Clean product category
df["product_category"] = (
    df["product_category"]
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.title()
)

category_mapping = {
    "Elec": "Electronics",
    "HOME": "Home & Kitchen",
    "Home": "Home & Kitchen",

}

df["product_category"] = df["product_category"].replace(category_mapping)

#Clean order date
df["order_date"] = (
    df["order_date"]
    .astype(str)
    .str.strip()
    .str.replace(".", "-", regex=False)
    .str.replace("/", "-", regex=False)

)

#converts the order_date column into real date values that pandas can understand
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce", dayfirst=False)

#Clean quantity
quantity_mapping = {
    "ONE": "1",
    "one": "1",
    "ten": "10",
    "TEN": "10",
}


df["quantity"] = (
    df["quantity"]
    .astype(str)
    .str.strip()
    .replace(quantity_mapping)
)

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

#Clean unit price
df["unit_price_sek"] = (
    df["unit_price_sek"]
    .astype(str)
    .str.strip()
    .str.replace("SEK", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace(" ", "", regex=False)                 
)

df["unit_price_sek"] = pd.to_numeric(df["unit_price_sek"], errors="coerce")

#Clean payment status
df["payment_status"] = (
    df["payment_status"]
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.title()
)

payment_mapping = {
    "Payment Failed": "Failed"
}

df["payment_status"] = df["payment_status"].replace(payment_mapping)

#Clean delivery status
df["delivery_status"] = (
    df["delivery_status"]
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.title()
)

delivery_mapping = {
    "Canceled": "Cancelled"

}

df["delivery_status"] = df["delivery_status"].replace(delivery_mapping)

#Add calculated column
df["total_order_value_sek"] = df["quantity"] * df["unit_price_sek"]

df = df.dropna(subset=[
    "order_id",
    "customer_name",
    "country",
    "product_category",
    "order_date",
    "quantity",
    "unit_price_sek"
])

#Save cleaned data
df.to_csv("data/cleaned_orders_data.csv", index=False)

print("Data cleaning complete.")
print("Rows after cleaning: {len(df)}")
print(df.head())