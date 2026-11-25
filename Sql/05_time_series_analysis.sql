USE retail_analytics;

-- Monthly Revenue
SELECT
    YearMonth,
    SUM(Revenue) AS Monthly_Revenue
FROM retail_sales
GROUP BY YearMonth
ORDER BY YearMonth;


-- Monthly Revenue and Previous Month Revenue
SELECT
    YearMonth,
    SUM(Revenue) AS Monthly_Revenue,
    LAG(SUM(Revenue)) OVER (
        ORDER BY YearMonth
    ) AS Previous_Month_Revenue
FROM retail_sales
GROUP BY YearMonth
ORDER BY YearMonth;


-- Month-over-Month Growth Percentage
WITH MonthlySales AS (
    SELECT
        YearMonth,
        SUM(Revenue) AS Monthly_Revenue
    FROM retail_sales
    GROUP BY YearMonth
),
MonthlyGrowth AS (
    SELECT
        YearMonth,
        Monthly_Revenue,
        LAG(Monthly_Revenue) OVER (
            ORDER BY YearMonth
        ) AS Previous_Month_Revenue
    FROM MonthlySales
)
SELECT
    YearMonth,
    Monthly_Revenue,
    Previous_Month_Revenue,
    ROUND(
        (Monthly_Revenue - Previous_Month_Revenue)
        / Previous_Month_Revenue * 100,
        2
    ) AS Growth_Percentage
FROM MonthlyGrowth
ORDER BY YearMonth;