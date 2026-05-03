# Online_orders_dataops_project# Online Orders DataOps Project

## Project Overview

This project is a small DataOps / data cleaning project using online order data.

The goal of the project is to take messy order data from a Google Sheet, clean it using Python and pandas, and prepare it for analysis.

The dataset contains information about customer orders, such as order ID, customer name, product category, order date, quantity, unit price, payment status, and delivery status.

## Dataset

The dataset is stored in a Google Sheet and contains online order data.

Example columns:

| Column Name        | Description                                                     |
| ------------------ | --------------------------------------------------------------- |
| `order_id`         | Unique ID for each order                                        |
| `customer_name`    | Name of the customer                                            |
| `product_category` | Category of the product ordered                                 |
| `order_date`       | Date when the order was placed                                  |
| `quantity`         | Number of items ordered                                         |
| `unit_price_sek`   | Price per item in Swedish kronor                                |
| `payment_status`   | Whether the payment was paid, pending, or failed                |
| `delivery_status`  | Whether the order was delivered, shipped, pending, or cancelled |

## Project Goals

The main goals of this project are to:

- Load order data into Python
- Clean messy column names
- Clean customer names
- Standardize text values
- Handle missing or inconsistent data
- Prepare the data for analysis
- Practice a simple DataOps workflow

## Technologies Used

- Python
- pandas
- Google Sheets
- VS Code
- Git
- GitHub

## Data Cleaning Steps

The project includes several data cleaning steps.

### 1. Clean Column Names

Column names are cleaned by removing extra spaces and converting them to lowercase.

```python
df.columns = df.columns.str.strip().str.lower()
```
