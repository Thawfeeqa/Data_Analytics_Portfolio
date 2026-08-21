create database dataco_supply_chain;
use dataco_supply_chain;
SELECT 
    `Shipping Mode`,
    COUNT(*) AS Total_Orders,
    SUM(`Late_delivery_risk`) AS Late_Orders,
    ROUND(AVG(`Late_delivery_risk`) * 100, 1) AS Late_Pct
FROM `datacosupplychain_clean_sql`
GROUP BY `Shipping Mode`
ORDER BY Late_Pct DESC;
SELECT 
    `Market`,
    ROUND(SUM(`Order Profit Per Order`), 2) AS Total_Profit,
    COUNT(*) AS Total_Orders
FROM `datacosupplychain_clean_sql`
GROUP BY `Market`
ORDER BY Total_Profit DESC;
SELECT 
    `Category Name`,
    ROUND(AVG(`Order Profit Per Order`), 2) AS Avg_Profit,
    COUNT(*) AS Total_Orders
FROM `datacosupplychain_clean_sql`
GROUP BY `Category Name`
HAVING AVG(`Order Profit Per Order`) < 0
ORDER BY Avg_Profit ASC;
SELECT 
    `Customer Id`,
    `Customer Fname`,
    ROUND(SUM(`Sales`), 2) AS Total_Revenue
FROM `datacosupplychain_clean_sql`
GROUP BY `Customer Id`, `Customer Fname`
ORDER BY Total_Revenue DESC
LIMIT 10;
SELECT 
    YEAR(`order date (DateOrders)`) AS Year,
    MONTH(`order date (DateOrders)`) AS Month,
    ROUND(SUM(`Order Profit Per Order`), 2) AS Monthly_Profit
FROM `datacosupplychain_clean_sql`
GROUP BY 
    YEAR(`order date (DateOrders)`),
    MONTH(`order date (DateOrders)`)
ORDER BY Year, Month;