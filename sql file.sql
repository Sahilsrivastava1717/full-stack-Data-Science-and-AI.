create database if not exists  customer;

use customer;

create table information (
 orderid int primary key,
 customername varchar(50) not null,
 product varchar(50),
 category varchar(50),
 quantity int not null,
 unitprice int ,
 region varchar(50),
 totalamount int
 );
 
insert into information (
 orderid, customername, product, category, quantity, unitprice,region ,totalamount 
 )
 VALUES
('1000', 'Allison Hill', 'Monitor', 'Accessories', 4, 114.37, 'South', 457.48),
('1001', 'Noah Rhodes', 'Tablet', 'Accessories', 3, 307.8, 'East', 923.4),
('1002', 'Angie Henderson', 'Keyboard', 'Electronics', 4, 316.92, 'West', 1267.68),
('1003', 'Daniel Wagner', 'Tablet', 'Accessories', 5, 714.94, 'North', 2859.76),
('1004', 'Cristian Santos', 'Tablet', 'Electronics', 1, 649.00, 'South', 649.00),
('1005', 'Connie Lawrence', 'Mouse', 'Electronics', 3, 849.88, 'West', 2549.64),
('1006', 'Abigail Shaffer', 'Keyboard', 'Electronics', 1, 256.03, 'North', 256.03),
('1007', 'Gina Moore', 'Keyboard', 'Electronics', 3, 451.95, 'West', 1355.85),
('1008', 'Gabrielle Davis', 'Keyboard', 'Electronics', 3, 264.01, 'North', 792.03),
('1009', 'Ryan Munoz', 'Tablet', 'Accessories', 1, 779.83, 'South', 779.83),
('1010', 'Monica Herrera', 'Monitor', 'Accessories', 1, 482.64, 'East', 482.64),
('1011', 'Jamie Arnold', 'Keyboard', 'Accessories', 3, 287.15, 'North', 861.45),
('1012', 'Lisa Hensley', 'Tablet', 'Accessories', 2, 610.93, 'West', 1221.86),
('1013', 'Michele Williams', 'Mouse', 'Accessories', 4, 128.18, 'South', 512.72),
('1014', 'Dylan Miller', 'Monitor', 'Electronics', 1, 858.06, 'North', 858.06),
('1015', 'Brian Ramirez', 'Mouse', 'Accessories', 4, 504.78, 'West', 2019.12),
('1016', 'Holly Wood', 'Monitor', 'Accessories', 2, 455.64, 'West', 911.28),
('1017', 'Derek Zuniga', 'Tablet', 'Electronics', 2, 933.99, 'West', 1867.98),
('1018', 'Lisa Jackson', 'Laptop', 'Accessories', 2, 754.54, 'North', 1509.08),
('1019', 'Carla Gray', 'Monitor', 'Electronics', 1, 393.89, 'North', 393.89);


select * from information;

-- Find total sales (TotalAmount) made in the 'North' region.
select totalamount 
from information
where region = 'North';

-- find the order(s) with the maximum TotalAmount.
select * 
from information 
where totalamount = (select max(totalamount) from information);

-- Group total sales by Category and show in descending order.
select sum(totalamount) , category as total_sales 
from information 
group by category
order by total_sales DESC ;
 
 
-- List customer names who ordered 'Laptop'.
select customername  
from information
where product = 'Laptop';

-- Find the top 3 regions with highest total sales.
SELECT region, SUM(totalamount) AS total_sales
FROM information
GROUP BY region
ORDER BY total_sales DESC
LIMIT 3;


