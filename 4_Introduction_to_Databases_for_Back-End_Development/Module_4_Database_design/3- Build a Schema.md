## Build a Schema (Restaurant) — Simple SQL

```sql
-- 1) Create database and select it
CREATE DATABASE IF NOT EXISTS restaurant;
USE restaurant;

-- 2) Core entities
CREATE TABLE tbl (
  table_id INT PRIMARY KEY,
  location VARCHAR(255) NOT NULL
);

CREATE TABLE waiter (
  waiter_id INT PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  contact_no VARCHAR(15),
  shift VARCHAR(10)
);

CREATE TABLE customer (
  customer_id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  NIC_no VARCHAR(12),
  contact_no VARCHAR(15)
);

-- 3) Orders (table + waiter)
CREATE TABLE table_order (
  order_id INT PRIMARY KEY,
  date_time DATETIME NOT NULL,
  table_id INT NOT NULL,
  waiter_id INT NOT NULL,
  FOREIGN KEY (table_id) REFERENCES tbl(table_id),
  FOREIGN KEY (waiter_id) REFERENCES waiter(waiter_id)
);

-- 4) Reservations (customer + table + order)
CREATE TABLE reservation (
  reservation_id INT PRIMARY KEY,
  date_time DATETIME NOT NULL,
  no_of_pax INT NOT NULL,
  order_id INT NOT NULL,
  table_id INT NOT NULL,
  customer_id INT NOT NULL,
  FOREIGN KEY (order_id) REFERENCES table_order(order_id),
  FOREIGN KEY (table_id) REFERENCES tbl(table_id),
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

-- 5) Menu and items
CREATE TABLE menu (
  menu_id INT PRIMARY KEY,
  description VARCHAR(255),
  availability TINYINT NOT NULL
);

CREATE TABLE menu_item (
  menu_item_id INT PRIMARY KEY,
  menu_id INT NOT NULL,
  description VARCHAR(255) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  availability TINYINT NOT NULL,
  FOREIGN KEY (menu_id) REFERENCES menu(menu_id)
);

-- 6) Order <> menu items (bridge)
CREATE TABLE order_menu_item (
  order_id INT NOT NULL,
  menu_item_id INT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (order_id, menu_item_id),
  FOREIGN KEY (order_id) REFERENCES table_order(order_id),
  FOREIGN KEY (menu_item_id) REFERENCES menu_item(menu_item_id)
);
```
