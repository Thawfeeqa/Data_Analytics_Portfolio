📊 DataCo Supply Chain Analytics

📌 Project Overview

This project is an end-to-end Data Analytics and Business Intelligence project based on the DataCo SMART Supply Chain Dataset.

The project analyzes sales performance, profitability, delivery reliability, shipping efficiency, customer contribution, market performance, and supply-chain risks using Python, SQL, Power BI, and Excel.

The primary objective is to transform raw supply-chain data into meaningful business insights that can support operational and management-level decision-making.

Project Workflow

Raw Data → Data Cleaning → Exploratory Data Analysis → SQL Business Analysis → Power BI Dashboard → Business Insights → Recommendations


---

🎯 Business Objectives

Analyze sales, revenue, profit, and order performance

Measure late-delivery risk and delivery performance

Evaluate shipping-mode efficiency

Analyze shipping delays across markets and product categories

Identify high-performing markets

Evaluate product-category profitability

Identify high-revenue customers

Analyze monthly profitability trends

Investigate factors associated with late deliveries

Develop interactive Power BI dashboards

Generate actionable business recommendations



---

📊 Dataset

Dataset: DataCo SMART Supply Chain for Big Data Analysis

Original Dataset Source:
DataCo SMART Supply Chain for Big Data Analysis – Kaggle

The original structured dataset contains approximately 180,519 records and includes supply-chain information related to customers, orders, products, sales, profit, shipping, markets, and delivery performance. 

Dataset Handling

The complete original dataset was used locally for the project analysis and Power BI dashboard development.

Due to repository size considerations, the complete original dataset is not uploaded to GitHub.

Instead, this repository contains:

Raw Data Sample — a representative sample taken from the original dataset

Cleaned Data Sample — the corresponding cleaned sample used to demonstrate the data-cleaning workflow


The sample datasets are provided for reference, reproducibility of the workflow, and demonstration purposes.


---

🐍 Python — Data Cleaning & Exploratory Data Analysis

Python was used for data inspection, data-quality analysis, cleaning, transformation, and exploratory data analysis (EDA).

Libraries Used

Python

Pandas

Matplotlib

Seaborn


Data Inspection

The following checks were performed:

Dataset shape and structure

Missing-value analysis

Duplicate-row analysis

Data-type validation

Descriptive statistics

Unique-value analysis

Initial data inspection


Data Cleaning

The following unnecessary or sensitive columns were removed:

Product Description

Order Zipcode

Customer Email

Customer Password

Product Image

Customer Street


Missing values in Customer Lname were handled by replacing them with Unknown.

Order and shipping date fields were converted into proper datetime format.

The cleaned dataset was then exported for further analysis.


---

📈 Python Visualizations

Four exploratory visualizations were created using Matplotlib and Seaborn.

1. Delivery Status Distribution

Analyzes the distribution of orders across different delivery statuses.

2. Late Delivery Risk

Compares orders with and without identified late-delivery risk.

3. Orders by Shipping Mode

Analyzes order volume across different shipping modes.

4. Sales Distribution

Examines the distribution of sales values across transactions using a histogram and density visualization.

These visualizations provide an initial understanding of delivery performance, shipping patterns, risk levels, and sales distribution.


---

🗄️ SQL — Business Analysis

MySQL was used to perform business-focused analysis on the cleaned dataset.

SQL Concepts Demonstrated

CREATE DATABASE

USE

SELECT

COUNT()

SUM()

AVG()

ROUND()

GROUP BY

HAVING

ORDER BY

LIMIT

YEAR()

MONTH()


Business Analysis Performed

1. Shipping Mode Performance

Analyzed:

Total orders

Late orders

Late-delivery percentage


by shipping mode.

2. Profit by Market

Calculated:

Total profit

Total orders


for each market and ranked markets based on profitability.

3. Category Profitability

Analyzed average profit per order by product category and identified categories with negative average profitability.

4. Top 10 Customers

Ranked customers based on total revenue contribution to identify high-value customers.

5. Monthly Profit Trend

Calculated monthly profit using year and month extracted from the order date to evaluate profitability trends over time.


---

📊 Power BI Dashboard

Power BI was used to develop an interactive Supply Chain Business Intelligence Dashboard.

The Power BI dashboard consists of three analytical pages:

1️⃣ Executive Overview

Provides a high-level view of overall business performance.

KPIs

Total Revenue: $36.78M

Total Profit: $3.97M

Total Orders: 66K

Late Delivery: 54.83%


Dashboard Visuals

Sales by Market

Sales and Profit Trend

Late Delivery % by Shipping Mode

Profit by Category

Orders by Customer Segment

Orders by Delivery Status



---

2️⃣ Shipping Performance

Focuses on shipping efficiency and delivery performance.

KPIs

Total Orders: 66K

Late Orders: 36K

Average Shipping Days: 3.50 days

Average Shipping Delay: 0.57 days


Dashboard Visuals

Late Delivery % over Time

Average Shipping Delay by Market

Average Shipping Delay by Shipping Mode

Average Shipping Delay by Category

Orders by Shipping Mode

Average Shipping Delay Trend



---

3️⃣ Root Cause Drill-Down

Focuses on investigating factors associated with delivery risk.

KPIs

Late Orders: 36K

Average Shipping Days: 3.50 days

Late Delivery %: 54.83%

Average Shipping Delay: 0.57 days


Dashboard Visuals

Decomposition Tree

Late Orders by Market

Late Delivery % by Shipping Mode

Late Delivery % by Market and Shipping Mode

Geographic Delivery-Risk Analysis

Market-Level Comparisons


The Decomposition Tree provides interactive drill-down analysis to investigate delivery-risk patterns across different business dimensions.


---

📸 Power BI Dashboard Screenshots

Screenshots of the Power BI dashboards are included separately for portfolio presentation and visual reference.

The screenshots represent:

Executive Overview

Shipping Performance

Root Cause Drill-Down



---

📌 Key Business Insights

1. Delivery Performance is a Major Operational Concern

The overall late-delivery rate is approximately 54.83%, indicating a significant delivery-performance challenge.

2. Shipping Delay Exists

The average shipping delay is approximately 0.57 days, meaning actual shipping time exceeds scheduled shipping time by roughly half a day on average.

3. Shipping Mode Influences Delivery Risk

Different shipping modes demonstrate different levels of late-delivery risk. Shipping-mode selection should therefore be evaluated alongside operational capacity and delivery commitments.

4. Standard Class Handles High Order Volume

Standard Class represents a significant portion of order volume. Improving performance in this high-volume segment could have a meaningful impact on overall supply-chain efficiency.

5. Market Profitability Varies

Profit contribution differs across markets. Market-level analysis helps identify stronger-performing regions and areas requiring further investigation.

6. High-Value Customers are Important

The top-customer analysis identifies customers contributing significant revenue, highlighting the importance of customer retention and service quality.

7. Sales Distribution Contains High-Value Transactions

The sales distribution shows that most transactions occur at relatively lower sales values, while a smaller number of high-value transactions contribute significantly to overall sales.


---

💡 Business Recommendations

Based on the analysis:

Investigate high-risk shipping modes and their operational causes.

Reduce the average shipping delay of approximately 0.57 days.

Analyze late deliveries by market to identify geographic bottlenecks.

Closely monitor high-volume shipping segments.

Improve delivery planning for high-risk markets and shipping modes.

Protect high-value customers through proactive service monitoring.

Investigate high-value transactions to understand their business drivers.

Monitor monthly profitability trends.

Use Power BI drill-down analysis to investigate delivery-risk factors.

Continuously monitor delivery KPIs to measure operational improvements.



---

🛠️ Tools & Technologies

Technology	Purpose

Python	Data Cleaning & Exploratory Data Analysis
Pandas	Data Manipulation
Matplotlib	Data Visualization
Seaborn	Exploratory Visualization
MySQL	Business Analysis
Power BI	Interactive Dashboard Development
Excel	Dataset Preparation
GitHub	Portfolio & Project Documentation



---

🔄 End-to-End Workflow

Original Raw Dataset
        ↓
Data Inspection
        ↓
Python Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Cleaned Dataset
        ↓
MySQL Business Analysis
        ↓
Power BI Data Analysis
        ↓
Interactive Dashboard Development
        ↓
Business Insights
        ↓
Business Recommendations


---

📁 Repository Structure

Data-Analytics-Portfolio/
│
├── README.md
│
├── 01_Data_Sample/
│   └── DataCo_Sample
│
├── 02_Data_Cleaned_Sample/
│   └── DataCo_Cleaned_Sample
│
├── 03_Python/
│   └── end_to_end_project.py
│
├── 04_Visualizations/
│   ├── Delivery_Status.png
│   ├── Late_Delivery_Risk.png
│   ├── Shipping_Mode.png
│   └── Sales_Distribution.png
│
├── 05_SQL/
│   └── dataco_supply_chain_analysis.sql
│
├── 06_PowerBI/
│   ├── DataCo_Supply_Chain.pbix
│   │
│   ├── Executive_Overview/
│   │   └── Executive_Overview.png
│   │
│   ├── Shipping_Performance/
│   │   └── Shipping_Performance.png
│   │
│   └── Root_Cause_Drill_Down/
│       └── Root_Cause_Drill_Down.png
│
└── 07_Report/
    └── DataCo_Global_Supply_Chain_Final_Report.pdf

The repository is organized into separate sections for sample data, cleaned sample data, Python analysis, Python-generated visualizations, SQL business analysis, Power BI dashboard files and dashboard pages, and the final project report.


---

🎓 Project Outcome

This project demonstrates a complete end-to-end Data Analyst workflow, from raw data preparation and exploratory analysis to SQL business analysis, Power BI dashboard development, business insights, and recommendations.

Skills Demonstrated

Data Cleaning

Data Preprocessing

Exploratory Data Analysis

Python

Pandas

Matplotlib

Seaborn

SQL

MySQL

Power BI

Excel

Data Visualization

KPI Development

Business Analysis

Root Cause Analysis

Dashboard Development

Business Insight Generation

Data-Driven Recommendations


The final analytical solution transforms a large supply-chain dataset into an interactive business intelligence solution that helps stakeholders understand revenue, profitability, delivery performance, shipping efficiency, customer contribution, market performance, and operational risk.


---

👩‍💻 Author

Thawfeeqa S.

Aspiring Data Analyst

Technical Skills

Python | SQL | MySQL | Power BI | Excel | Data Visualization

Project

DataCo Supply Chain Analytics

This project is part of my Data Analytics Portfolio and demonstrates practical experience in **data cleaning, exploratory data analysis, SQL business analysis, Power BI dashboard development, data visualization, and business insight generation.
