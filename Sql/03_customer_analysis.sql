USE retail_analytics_new;

-- Top 10 Customers by Spending
SELECT
    CustomerID,
    SUM(Revenue) AS Total_Spending
FROM retail_sales
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY Total_Spending DESC
LIMIT 10;


-- Top 10 Customers by Number of Orders
SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders
FROM retail_sales
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY Total_Orders DESC
LIMIT 10;


-- Average Order Value
SELECT
    ROUND(
        SUM(Revenue) / COUNT(DISTINCT InvoiceNo),
        2
    ) AS Average_Order_Value
FROM retail_sales;


-- Customer Revenue Summary
SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity,
    SUM(Revenue) AS Total_Spending,
    ROUND(AVG(Revenue), 2) AS Average_Transaction_Revenue
FROM retail_sales
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY Total_Spending DESC
LIMIT 10;