# 🛍️ Retail Sales & Customer Analytics

An end-to-end data analytics project focused on analyzing retail transactions, identifying sales trends, understanding customer purchasing behavior, evaluating product performance, and generating business insights using Python, SQL, Pandas, and Streamlit.

The project transforms raw retail transaction data into meaningful business insights through data cleaning, exploratory data analysis, SQL queries, data visualization, customer segmentation, and an interactive dashboard.

---

## 📌 Project Overview

Retail businesses generate large amounts of transactional data every day. However, raw sales data alone does not provide meaningful information about business performance.

This project analyzes retail transaction data to identify:

- Products generating the highest revenue
- Countries contributing the most to sales
- Monthly sales trends and seasonal patterns
- Customer purchasing behavior
- Customer spending patterns and value
- Product and category performance
- Business opportunities through data-driven insights

The project combines Python-based data analysis, SQL querying, interactive visualizations, and a Streamlit dashboard to make the analysis easier to understand and explore.

---

## 🎯 Problem Statement

Retail businesses need to understand their sales performance, customer behavior, and product demand to make informed business decisions.

Analyzing raw transactional data manually can be time-consuming and difficult. Therefore, this project aims to process and analyze retail sales data to uncover meaningful patterns, identify important business metrics, and provide insights that can support better decision-making.

---

## 🎯 Objectives

- Clean and preprocess raw retail transaction data.
- Perform exploratory data analysis using Python.
- Analyze retail sales data using SQL.
- Identify top-performing products based on revenue.
- Analyze sales performance across different countries.
- Understand monthly sales trends.
- Evaluate customer purchasing behavior.
- Calculate important business metrics.
- Segment customers based on spending behavior.
- Create meaningful data visualizations.
- Develop an interactive dashboard using Streamlit.
- Generate business insights from the analyzed data.

---

## 📊 Dataset

**Dataset:** Online Retail Dataset

**Source:** UCI Machine Learning Repository / Online Retail Dataset

The dataset contains transactional information from an online retail business.

### Dataset Information

The dataset includes information such as:

| Column | Description |
|---|---|
| InvoiceNo | Unique invoice or transaction identifier |
| StockCode | Product identification code |
| Description | Product description |
| Quantity | Quantity of products purchased |
| InvoiceDate | Date and time of transaction |
| UnitPrice | Price per unit |
| CustomerID | Unique customer identifier |
| Country | Country where the customer is located |

### Data Preparation

The raw dataset was processed before analysis.

Data cleaning included:

- Handling missing values
- Removing invalid records
- Filtering inappropriate transaction records
- Preparing data for analysis
- Converting and handling date information
- Creating calculated columns
- Calculating revenue for transactions

A cleaned dataset was created and used for further analysis.

### Revenue Calculation

Revenue was calculated using:

`Revenue = Quantity × UnitPrice`

This calculated column was used throughout the project to analyze sales performance.

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Data Analysis
- Pandas
- NumPy

### Database & Querying
- MySQL
- SQL

### Data Visualization
- Plotly
- Matplotlib
- Seaborn

### Dashboard Development
- Streamlit

### Development Environment
- Jupyter Notebook
- Anaconda
- MySQL Workbench

### Version Control
- Git
- GitHub

---

## 📁 Project Structure

```text
Retail Sales & Customer Analytics/
│
├── Dashboard/
│   └── app.py
│
├── Data/
│   ├── Online Retail.xlsx
│   └── Cleaned Dataset
│
├── notebooks/
│   ├── Retail Sales Analytics.ipynb
│   └── CleanRetailSales.csv
│
├── reports/
│   └── Retail_Sales_Customer_Analytics_Report.pdf
│
├── Sql/
│   └── SQL Analysis Queries
│
├── visualizations/
│   └── Analysis Graphs
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 Project Workflow

### Phase 1: Data Collection

- Downloaded the Online Retail dataset.
- Imported the dataset into the Python environment using Pandas.
- Explored the dataset structure, columns, data types, and records.

### Phase 2: Data Cleaning & Preprocessing

- Inspected missing values.
- Identified invalid and unsuitable records.
- Cleaned the dataset.
- Prepared transaction data for analysis.
- Created calculated columns such as Revenue.
- Saved the cleaned dataset for reuse.

### Phase 3: Exploratory Data Analysis (EDA)

Performed exploratory analysis using Python and Pandas.

Analysis included:

- Understanding the dataset structure
- Examining missing values
- Exploring unique products, customers, and countries
- Analyzing transaction records
- Calculating total revenue
- Grouping data for business analysis
- Identifying top-performing products
- Analyzing customer spending

### Phase 4: SQL Analysis

Used MySQL to perform structured queries and business analysis.

SQL concepts utilized include:

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- Aggregate functions
- Filtering and sorting
- Business-oriented queries

SQL was used to extract, summarize, and analyze information from retail sales data.

### Phase 5: Business Analysis

The project explored several business questions:

#### 1. Sales Performance Analysis
- What is the overall revenue?
- How are sales performing over time?
- Which months generate higher sales?

#### 2. Product Analysis
- Which products generate the highest revenue?
- Which products perform best?
- What products contribute significantly to total sales?

#### 3. Country Analysis
- Which countries contribute the most revenue?
- How is revenue distributed across countries?
- Which markets are important for the business?

#### 4. Customer Analysis
- How much do customers spend?
- Who are the most valuable customers?
- What is the average customer spending?
- How frequently do customers purchase?

#### 5. Customer Segmentation
Customers were categorized according to spending behavior to understand different customer groups.

### Phase 6: Data Visualization

Created visualizations to make the results easier to understand.

Visualizations include:

- Monthly Sales Trend
- Top 10 Products by Revenue
- Country-wise Sales Analysis
- Customer Spending Analysis
- Customer Segmentation

Visualizations were created using Python visualization libraries and incorporated into the analysis.

### Phase 7: Interactive Dashboard

Developed an interactive dashboard using Streamlit.

The dashboard combines important sales metrics, visualizations, filters, and business insights in a single interface.

---

## 📈 Dashboard Features

### 1. Interactive Filters

The dashboard provides filters that allow users to explore the data dynamically.

- Country filter
- Month filter
- Reset filters option

The dashboard updates its metrics, visualizations, and business insights based on the selected filters.

### 2. Key Performance Indicators (KPIs)

The dashboard displays important business metrics:

- **Total Revenue:** Total sales revenue generated.
- **Total Orders:** Number of unique invoices.
- **Total Customers:** Number of unique customers.
- **Total Products:** Number of unique products.
- **Sales Growth:** Percentage change in sales compared with the previous period.

### 3. Monthly Sales Trend

A line chart showing sales performance across months.

This helps identify:

- Sales trends over time
- High-performing months
- Changes in revenue
- Seasonal patterns

### 4. Top 10 Products

A horizontal bar chart showing the top 10 products based on revenue.

This helps identify products that contribute significantly to total sales.

### 5. Country-wise Sales Distribution

A donut chart showing revenue contribution by country.

The visualization displays the leading countries and groups the remaining countries into an **Others** category for easier comparison.

### 6. Customer Analysis

Customer-related metrics include:

- Average Order Value (AOV)
- Customer Lifetime Value (CLV) / Average Customer Revenue

These metrics help understand purchasing behavior and customer value.

### 7. Customer Segmentation

Customers are categorized into three spending segments:

| Segment | Spending |
|---|---|
| Occasional | ≤ £100 |
| Regular | £100 – £500 |
| Premium | > £500 |

The segmentation visualization helps understand the distribution of customers across different spending groups.

### 8. Business Insights

The dashboard dynamically generates business insights based on the selected data and filters.

Examples of insights include:

- Top-performing country
- Best-performing month
- Revenue-related observations
- Customer-related observations

These insights help users interpret the results instead of viewing charts and metrics alone.

### 9. Data Download

Users can download the filtered dataset as a CSV file.

This allows users to save and further analyze the selected data.

---

## 💡 Business Value

The analysis can help retail businesses:

- Identify high-revenue products.
- Understand sales performance over time.
- Identify important geographical markets.
- Understand customer spending patterns.
- Identify high-value customer segments.
- Support inventory and product planning.
- Improve business decision-making.
- Monitor important sales metrics.
- Make data-driven business decisions.

---

## ▶️ How to Run the Project

### Prerequisites

Install the following:

- Python
- Anaconda (recommended)
- Jupyter Notebook
- MySQL
- Required Python libraries

### Step 1: Clone the Repository

```bash
git clone https://github.com/rajdaniel808-maker/Retail-Sales-and-Customer-Analytics.git
```

Navigate into the project directory:

```bash
cd Retail-Sales-Customer-Analytics
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Jupyter Notebook

Open Anaconda Navigator and launch Jupyter Notebook.

Navigate to:

```text
notebooks/
```

Open:

```text
Retail Sales Analytics.ipynb
```

Run the notebook cells to explore the data cleaning process, analysis, and visualizations.

### Step 4: Run SQL Analysis

Open MySQL Workbench.

Navigate to the SQL scripts in:

```text
Sql/
```

Execute the queries to perform the sales and customer analysis.

### Step 5: Run the Streamlit Dashboard

Navigate to the Dashboard folder:

```bash
cd Dashboard
```

Run the application:

```bash
streamlit run app.py
```

The dashboard will open in your web browser.

---

## 📌 Key Metrics

| Metric | Description |
|---|---|
| Revenue | Total revenue generated from sales |
| Orders | Unique invoice count |
| Customers | Unique customer count |
| Products | Unique products sold |
| Sales Growth | Percentage change in sales between periods |
| Average Order Value (AOV) | Average revenue generated per order |
| Customer Value | Average revenue generated per customer |

---

## 📷 Project Screenshots

Dashboard screenshots will be added here.

### Dashboard Overview

<!-- Add dashboard screenshot here -->

### Monthly Sales Trend

<!-- Add monthly sales screenshot here -->

### Top 10 Products

<!-- Add top products screenshot here -->

### Country-wise Sales

<!-- Add country sales screenshot here -->

### Customer Segmentation

<!-- Add customer segmentation screenshot here -->

---

## 📄 Project Report

A detailed project report is available in the `reports/` folder.

The report includes:

- Introduction
- Problem Statement
- Objectives
- Dataset Overview
- Technologies Used
- Project Workflow
- Business Analysis
- Dashboard Features
- Metrics
- Business Insights
- Conclusion
- Future Enhancements

---

## 🚀 Future Enhancements

Possible future improvements include:

- Sales forecasting using Machine Learning.
- Customer purchase prediction.
- Advanced customer segmentation.
- Product recommendation systems.
- Automated report generation.
- Additional dashboard filters.
- Advanced business intelligence metrics.

---

## 👨‍💻 Author

**B. Joseph Daniel Raj**

BSc Computer Science & Machine Learning

---

## 📌 Conclusion

Retail Sales & Customer Analytics demonstrates how raw transactional data can be transformed into meaningful business insights using data analytics tools.

By combining Python, Pandas, SQL, data visualization, and Streamlit, this project provides an analytical workflow for understanding retail sales performance, customer purchasing behavior, product revenue, and business trends.

The interactive dashboard makes the analysis accessible and allows users to explore sales data dynamically, supporting data-driven decision-making.