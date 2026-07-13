USE cloudcore_fpa;

-- ===========================================
-- Departments
-- ===========================================

INSERT INTO departments (department_name)
VALUES
('Sales'),
('Marketing'),
('Engineering'),
('Customer Success'),
('Finance'),
('HR'),
('IT'),
('Operations');

-- ===========================================
-- Regions
-- ===========================================

INSERT INTO regions (region_name)
VALUES
('North America'),
('Europe'),
('APAC'),
('Latin America');

-- ===========================================
-- Products
-- ===========================================

INSERT INTO products
(product_name, subscription_type, monthly_price)
VALUES
('Starter','Monthly',49.00),
('Professional','Monthly',149.00),
('Business','Monthly',399.00),
('Enterprise','Annual',2999.00);