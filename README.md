# 🛍️ Customer Shopping Behavior Analysis

An end-to-end data analytics project analyzing 3,900 customer transactions to uncover insights on spending patterns, product preferences, customer segmentation, and subscription behavior.

---

## 📌 Project Overview

This project follows a complete analytics pipeline:

**Python (EDA & Cleaning)** → **MySQL (SQL Analysis)** → **Power BI (Dashboard)**

---

## 🗂️ Dataset

| Property | Details |
|---|---|
| Rows | 3,900 |
| Columns | 18 |
| Source | customer_shopping_behavior.csv |

**Key fields:** Customer ID, Age, Gender, Item Purchased, Category, Purchase Amount, Review Rating, Shipping Type, Subscription Status, Discount Applied, Previous Purchases, Frequency of Purchases

---

## 🐍 Python – Exploratory Data Analysis (`project_1.py`)

- Loaded dataset using **Pandas** and explored structure with `.info()` and `.describe()`
- **Missing Data:** Imputed 37 null values in `review_rating` using per-category median
- **Column Standardization:** Renamed all columns to snake_case
- **Feature Engineering:**
  - `age_group` — binned ages into Young Adult / Adult / Middle-Age / Senior using `pd.qcut()`
  - `purchase_frequency_days` — mapped frequency labels to numeric day values
- **Redundancy Check:** Confirmed `discount_applied` and `promo_code_used` were identical; dropped `promo_code_used`

---

## 🗄️ MySQL – Data Upload (`uploadsql.py`)

- Connected Python to MySQL using **SQLAlchemy** (`mysql+pymysql`)
- Uploaded cleaned DataFrame to `customer_shopping` table via `df.to_sql()`

---

## 🔍 SQL – Business Analysis (`customer_behavior_sql_queries.sql`)

10 queries written in MySQL answering key business questions:

| # | Question |
|---|---|
| Q1 | Total revenue by gender |
| Q2 | High-spending discount users (above avg purchase) |
| Q3 | Top 5 products by average review rating |
| Q4 | Avg purchase amount: Standard vs Express shipping |
| Q5 | Subscribers vs non-subscribers — avg spend & total revenue |
| Q6 | Top 5 products by discount usage rate |
| Q7 | Customer segmentation — New / Returning / Loyal |
| Q8 | Top 3 most purchased products per category (window function) |
| Q9 | Repeat buyers (>5 purchases) and subscription likelihood |
| Q10 | Revenue contribution by age group |

**Concepts used:** GROUP BY, Subqueries, CTEs, Window Functions (`ROW_NUMBER() OVER`), CASE WHEN, ROUND, aggregation

---

## 📊 Power BI – Dashboard

Interactive dashboard with dynamic slicers allowing users to filter all visuals simultaneously.

**Slicers:**
- Subscription Status (Yes / No)
- Gender (Male / Female)
- Category (Accessories / Clothing / Footwear / Outerwear)
- Shipping Type (2-Day Shipping / Express / Free Shipping / Next Day Air / Standard)

**Visuals included:**
- Key Performance Indicator Cards — Total Customers, Average Purchase Amount, Average Review Rating
- Donut Chart — Percentage of Customers by Subscription Status
- Bar Charts — Revenue and Sales by Category
- Horizontal Bar Charts — Revenue and Sales by Age Group

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Python (Pandas) | Data cleaning & feature engineering |
| SQLAlchemy + PyMySQL | Python–MySQL connection |
| MySQL | SQL-based business analysis |
| Power BI | Interactive dashboard |

---

## 📁 File Structure

```
├── project_1.py                      # EDA and data cleaning
├── uploadsql.py                      # Upload cleaned data to MySQL
├── customer_behavior_sql_queries.sql # 10 business SQL queries
├── Customer_Shopping_Behavior_Analysis.pdf  # Full project report
└── README.md
```

---

## 💡 Key Insights

- **Male customers** generated significantly higher revenue than female customers
- **73% of customers** are non-subscribers, yet their total revenue exceeds subscribers
- **Young Adults** are the top revenue-contributing age group
- **Express shipping** users spend slightly more on average than Standard
- **Loyal customers** (>10 previous purchases) make up the largest customer segment (3,116)
- **Hat** has the highest discount dependency rate (~50%)
