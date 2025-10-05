## Primary Key vs Foreign Key (Quick Guide)

- Primary Key: uniquely identifies a row in a table. Must be unique and not null.
- Foreign Key: references a key in another table to enforce relationships and integrity.

Key points:

- A table typically has one primary key (can be composite).
- A foreign key points to a candidate key (often the primary key) in a parent table.
- Foreign keys can define actions: ON DELETE/UPDATE CASCADE, SET NULL, or RESTRICT.

Minimal example (SQL):

```sql
CREATE TABLE authors (
  author_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE books (
  book_id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  author_id INT NOT NULL,
  CONSTRAINT books_author
    FOREIGN KEY (author_id)
    REFERENCES authors(author_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
```
