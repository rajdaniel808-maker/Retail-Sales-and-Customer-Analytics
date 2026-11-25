USE retail_analytics;

-- Top 10 Products by Revenue
SELECT
    Description,
    SUM(Revenue) AS Total_Revenue
FROM retail_sales
GROUP BY Description
ORDER BY Total_Revenue DESC
LIMIT 10;


-- Top 10 Products by Quantity Sold
SELECT
    Description,
    SUM(Quantity) AS Total_Quantity
FROM retail_sales
GROUP BY Description
ORDER BY Total_Quantity DESC
LIMIT 10;


-- Lowest Revenue Products
SELECT
    Description,
    SUM(Revenue) AS Total_Revenue
FROM retail_sales
GROUP BY Description
ORDER BY Total_Revenue ASC
LIMIT 10;


-- Revenue Contribution of Top 10 Products
SELECT
    Description,
    SUM(Revenue) AS Product_Revenue,
    ROUND(
        SUM(Revenue) * 100 /
        (SELECT SUM(Revenue) FROM retail_sales),
        2
    ) AS Revenue_Percentage
FROM retail_sales
GROUP BY Description
ORDER BY Product_Revenue DESC
LIMIT 10;