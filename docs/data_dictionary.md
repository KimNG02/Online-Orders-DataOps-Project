# Data Dictionary: Online Orders Dataset

| Column                | Type    | Description                           | Example     |
| --------------------- | ------- | ------------------------------------- | ----------- |
| order_id              | Text    | Unique identifier for each order      | O001        |
| customer_name         | Text    | Name of the customer                  | Anna Lind   |
| country               | Text    | Country where the customer is located | Sweden      |
| product_category      | Text    | Category of the product ordered       | Electronics |
| order_date            | Date    | Date when the order was placed        | 2024-01-15  |
| quantity              | Integer | Number of items ordered               | 2           |
| unit_price_sek        | Numeric | Price of one item in SEK              | 199         |
| payment_status        | Text    | Payment state of the order            | Paid        |
| delivery_status       | Text    | Delivery state of the order           | Delivered   |
| total_order_value_sek | Numeric | Quantity multiplied by unit price     | 398         |
