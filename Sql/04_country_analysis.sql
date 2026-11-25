USE retail_analytics;

-- Revenue by Country
SELECT
    Country,
    SUM(Revenue) AS Total_Revenue
FROM retail_sales
GROUP BY Country
ORDER BY Total_Revenue DESC;


-- Customer Count by Country
SELECT
    Country,
    COUNT(DISTINCT CustomerID) AS Total_Customers
FROM retail_sales
GROUP BY Country
ORDER BY Total_Customers DESC;


-- Average Revenue per Customer by Country
SELECT
    Country,
    ROUND(
        SUM(Revenue) / COUNT(DISTINCT CustomerID),
        2
    ) AS Average_Revenue_Per_Customer
FROM retail_sales
GROUP BY Country
ORDER BY Average_Revenue_Per_Customer DESC;


-- Top 3 Products in Each Country
WITH ProductCountrySales AS (
    SELECT
        Country,
        Description,
        SUM(Revenue) AS Total_Revenue
    FROM retail_sales
    GROUP BY Country, Description
),
RankedProducts AS (
    SELECT
        Country,
        Description,
        Total_Revenue,
        RANK() OVER (
            PARTITION BY Country
            ORDER BY Total_Revenue DESC
        ) AS Product_Rank
    FROM ProductCountrySales
)
SELECT
    Country,
    Description,
    Total_Revenue,
    Product_Rank
FROM RankedProducts
WHERE Product_Rank <= 3
ORDER BY Country, Product_Rank;