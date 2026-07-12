-- ===========================================
-- CloudCore FP&A Database
-- 01 - Create Tables
-- Author: Your Name
-- ===========================================

USE cloudcore_fpa;

-- ===========================================
-- Products
-- ===========================================

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    subscription_type VARCHAR(30),
    monthly_price DECIMAL(10,2)
);

-- ===========================================
-- Regions
-- ===========================================

CREATE TABLE regions (
    region_id INT AUTO_INCREMENT PRIMARY KEY,
    region_name VARCHAR(50) NOT NULL
);

-- ===========================================
-- Departments
-- ===========================================

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);
-- ===========================================
-- Customers
-- ===========================================

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    industry VARCHAR(50),
    region_id INT,
    company_size VARCHAR(30),

    FOREIGN KEY (region_id)
        REFERENCES regions(region_id)
);

-- ===========================================
-- Employees
-- ===========================================

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    hire_date DATE,
    salary DECIMAL(10,2),

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- ===========================================
-- Revenue
-- ===========================================

CREATE TABLE revenue (
    revenue_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    revenue_date DATE,
    amount DECIMAL(12,2),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

-- ===========================================
-- Expenses
-- ===========================================

CREATE TABLE expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE,
    department_id INT,
    expense_type VARCHAR(50),
    amount DECIMAL(12,2),

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
-- ===========================================
-- Budget
-- ===========================================

CREATE TABLE budget (
    budget_id INT AUTO_INCREMENT PRIMARY KEY,
    budget_month DATE,
    department_id INT,
    budget_amount DECIMAL(12,2),

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);
-- ===========================================
-- Forecast
-- ===========================================

CREATE TABLE forecast (
    forecast_id INT AUTO_INCREMENT PRIMARY KEY,
    forecast_month DATE,
    expected_revenue DECIMAL(12,2)
);