# Online Orders DataOps Project

This is a small DataOps project built to practice working with data cleaning, SQL, PostgreSQL, Excel dashboards, and basic ETL workflows.

The project uses a sample online orders dataset created in Google Sheets. The goal is to transform messy spreadsheet data into a clean dataset that can be analyzed through Excel, SQL queries, and dashboards.

---

## Project Goal

The purpose of this project is to simulate a simple DataOps workflow:

1. Start with raw order data in Google Sheets
2. Export the data as a CSV file
3. Clean and standardize the data using Python and pandas
4. Save the cleaned dataset
5. Analyze the data using Excel dashboards and SQL
6. Document the dataset and workflow clearly

---

## Tools Used

- **Google Sheets** – used as the raw data source
- **Python** – used for data cleaning and transformation
- **pandas** – used to work with tabular data
- **PostgreSQL** – used as the relational database
- **SQL** – used for querying and creating analysis views
- **Excel** – used for pivot tables, charts, and dashboard creation
- **GitHub** – used for version control and project documentation

---

## Dataset Description

The dataset represents online customer orders.

Each row represents one order.

| Column                  | Description                                                   |
| ----------------------- | ------------------------------------------------------------- |
| `order_id`              | Unique ID for each order                                      |
| `customer_name`         | Name of the customer                                          |
| `country`               | Customer country                                              |
| `product_category`      | Category of the ordered product                               |
| `order_date`            | Date when the order was placed                                |
| `quantity`              | Number of items ordered                                       |
| `unit_price_sek`        | Price of one item in SEK                                      |
| `payment_status`        | Status of the payment                                         |
| `delivery_status`       | Status of the delivery                                        |
| `total_order_value_sek` | Total value of the order, calculated as quantity × unit price |

---

## Data Quality Issues

The raw dataset intentionally contains some messy values to simulate real-world spreadsheet data.

Examples of issues:

| Column             | Example issue                                                           |
| ------------------ | ----------------------------------------------------------------------- |
| `customer_name`    | Extra spaces, lowercase names, uppercase names                          |
| `country`          | Inconsistent values such as `SE`, `sweden`, `SWEDEN`                    |
| `product_category` | Inconsistent naming such as `Elec`, `electronics`, `ELECTRONICS`        |
| `order_date`       | Different date formats such as `2024/01/15`, `15-02-2024`, `2023.03.10` |
| `quantity`         | Text values such as `ONE`, `ten`, or extra spaces                       |
| `unit_price_sek`   | Values such as `1,299`, `249 SEK`, `2 499`                              |
| `payment_status`   | Different formats such as `paid`, `PAID`, `Payment Failed`              |
| `delivery_status`  | Different formats such as `delivered`, `DELIVERED`, `canceled`          |

These issues are cleaned and standardized using Python.

---

## Project Structure

```text
Online Orders DataOps Project/
│
├── data/
│   ├── raw_orders_data.csv
│   └── cleaned_orders_data.csv
│
├── dashboard/
│   └── online_orders_dashboard.xlsx
│
├── scripts/
│   └── clean_data.py
│
├── sql/
│   ├── create_tables.sql
│   ├── create_views.sql
│   └── analysis_queries.sql
│
├── docs/
│   └── data_dictionary.md
│
└── README.md
```
