# E-Commerce Growth Analytics & Customer Segmentation

## Overview
An end-to-end data analytics pipeline designed to extract actionable business intelligence from raw e-commerce transaction data. This project analyzes purchasing behavior to optimize retention strategies and identify operational bottlenecks.

## 🛠 Tech Stack
* **Data Cleaning & Pipeline:** Python (Pandas, NumPy)
* **Data Modeling & Queries:** PostgreSQL (CTEs, Window Functions)
* **Visualization:** Power BI / Advanced Excel

## 📊 Key Business Questions Answered
1. **Customer Segmentation:** Implemented an RFM (Recency, Frequency, Monetary) model to segment the user base into 'Champions', 'At-Risk', and 'Lost' categories.
2. **Operational Efficiency:** Engineered features to track delivery lag times, identifying structural delays in the supply chain.

## 📁 Repository Structure
* `data_cleaning.py`: Python script handling null values, timestamp conversion, and feature engineering.
* `rfm_analysis.sql`: Advanced SQL script utilizing Common Table Expressions (CTEs) and NTILE window functions to calculate RFM scores.

## 🚀 Impact
* Streamlined raw transactional data, removing outliers and establishing a clean schema for business intelligence tools.
* Provided a data-driven framework for marketing teams to target high-value "At-Risk" customers, potentially reducing churn.