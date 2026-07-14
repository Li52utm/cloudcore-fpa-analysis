USE cloudcore_fpa;

-- ===================================================
-- FP&A BUSINESS ANALYSIS QUERIES
-- CloudCore SaaS
-- ===================================================

-- =====================================
-- 1. Monthly Revenue
-- =====================================

SELECT
    DATE_FORMAT(revenue_date,'%Y-%m') AS Month,
    ROUND(SUM(amount),2) AS Revenue
FROM revenue
GROUP BY Month
ORDER BY Month;

-- =====================================
-- 2. Monthly Expenses
-- =====================================

SELECT
    DATE_FORMAT(expense_date,'%Y-%m') AS Month,
    ROUND(SUM(amount),2) AS Expenses
FROM expenses
GROUP BY Month
ORDER BY Month;

-- =====================================
-- 3. Revenue by Product
-- =====================================

SELECT
    product_id,
    ROUND(SUM(amount),2) AS Revenue
FROM revenue
GROUP BY product_id
ORDER BY Revenue DESC;

-- =====================================
-- 4. Top 10 Customers
-- =====================================

SELECT
    c.customer_name,
    ROUND(SUM(r.amount),2) AS Revenue
FROM revenue r
JOIN customers c
ON r.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY Revenue DESC
LIMIT 10;

-- =====================================
-- 5. Revenue by Industry
-- =====================================

SELECT
    c.industry,
    ROUND(SUM(r.amount),2) AS Revenue
FROM revenue r
JOIN customers c
ON r.customer_id = c.customer_id
GROUP BY c.industry
ORDER BY Revenue DESC;

-- =====================================
-- 6. Revenue by Region
-- =====================================

SELECT
    c.region_id,
    ROUND(SUM(r.amount),2) AS Revenue
FROM revenue r
JOIN customers c
ON r.customer_id = c.customer_id
GROUP BY c.region_id
ORDER BY Revenue DESC;

-- =====================================
-- 7. Average Revenue Per Customer
-- =====================================

SELECT
    ROUND(AVG(amount),2) AS Avg_Revenue
FROM revenue;

-- =====================================
-- 8. Total Revenue
-- =====================================

SELECT
    ROUND(SUM(amount),2) AS Total_Revenue
FROM revenue;

-- =====================================
-- 9. Total Expenses
-- =====================================

SELECT
    ROUND(SUM(amount),2) AS Total_Expenses
FROM expenses;

-- =====================================
-- 10. Monthly Transaction Count
-- =====================================

SELECT
    DATE_FORMAT(revenue_date,'%Y-%m') AS Month,
    COUNT(*) AS Transactions
FROM revenue
GROUP BY Month
ORDER BY Month;