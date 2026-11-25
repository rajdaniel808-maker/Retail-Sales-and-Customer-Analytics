CREATE database IF NOT EXISTS retail_analytics_new;
use retail_analytics_new;

CREATE TABLE retail_sales (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice DECIMAL(10,2),
    CustomerID INT,
    Country VARCHAR(100),
    Revenue DECIMAL(10,2)
);
ALTER TABLE retail_sales
ADD COLUMN YearMonth VARCHAR(10);
describe retail_sales;
SELECT COUNT(*) as Total_Records FROM retail_sales;