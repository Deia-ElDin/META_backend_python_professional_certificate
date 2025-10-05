## Table Relationships (Simple Guide)

### 1) One-to-One (1:1)

Definition: each row in table A relates to at most one row in table B, and vice versa.

Use a foreign key with UNIQUE (or share the same PK).

```sql
CREATE TABLE customer (
  customer_id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE customer_profile (
  profile_id INT PRIMARY KEY,
  customer_id INT UNIQUE NOT NULL,
  birthdate DATE,
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
```

### 2) One-to-Many (1:N)

Definition: one row in table A can relate to many rows in table B; each B belongs to one A.

Put the foreign key on the "many" side.

```sql
CREATE TABLE waiter (
  waiter_id INT PRIMARY KEY,
  name VARCHAR(150) NOT NULL
);

CREATE TABLE table_order (
  order_id INT PRIMARY KEY,
  waiter_id INT NOT NULL,
  FOREIGN KEY (waiter_id) REFERENCES waiter(waiter_id)
);
```

### 3) Many-to-Many (M:N)

Definition: rows in A can relate to many rows in B and vice versa; use a join table.

Use a join table with a composite primary key.

```sql
CREATE TABLE menu (
  menu_id INT PRIMARY KEY,
  description VARCHAR(255)
);

CREATE TABLE category (
  category_id INT PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE menu_category (
  menu_id INT NOT NULL,
  category_id INT NOT NULL,
  PRIMARY KEY (menu_id, category_id),
  FOREIGN KEY (menu_id) REFERENCES menu(menu_id),
  FOREIGN KEY (category_id) REFERENCES category(category_id)
);
```
