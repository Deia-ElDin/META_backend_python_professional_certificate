## Comparison Operators (SQL) — Examples and Results

Employee data used for comparisons:

| employee_id | employee_name | salary | allowance |
| ----------- | ------------- | ------ | --------- |
| 1           | Alex          | 24000  | 1000      |
| 2           | John          | 55000  | 1000      |
| 3           | James         | 52000  | 1000      |
| 4           | Sam           | 24000  | 1000      |

### Operator quick reference

| Operator           | Meaning                        | Example                           |
| ------------------ | ------------------------------ | --------------------------------- |
| =                  | equal                          | `salary = 24000`                  |
| <> or !=           | not equal                      | `salary <> 24000`                 |
| >, >=              | greater than, greater or equal | `salary >= 52000`                 |
| <, <=              | less than, less or equal       | `salary <= 24000`                 |
| BETWEEN ... AND    | inclusive range                | `salary BETWEEN 24000 AND 52000`  |
| IN (...)           | list membership                | `employee_name IN ('Alex','Sam')` |
| LIKE pattern       | pattern match                  | `employee_name LIKE 'J%'`         |
| IS NULL / NOT NULL | null checks                    | `allowance IS NOT NULL`           |

### Queries and results

| SQL                                                                 | Result                                         |
| ------------------------------------------------------------------- | ---------------------------------------------- |
| `SELECT * FROM employee WHERE salary = 24000;`                      | Rows: employee_id 1 (Alex), 4 (Sam)            |
| `SELECT * FROM employee WHERE salary <> 24000;`                     | Rows: employee_id 2 (John), 3 (James)          |
| `SELECT * FROM employee WHERE salary > 50000;`                      | Rows: employee_id 2 (John), 3 (James)          |
| `SELECT * FROM employee WHERE salary >= 52000;`                     | Rows: employee_id 2 (John), 3 (James)          |
| `SELECT * FROM employee WHERE salary < 30000;`                      | Rows: employee_id 1 (Alex), 4 (Sam)            |
| `SELECT * FROM employee WHERE salary <= 24000;`                     | Rows: employee_id 1 (Alex), 4 (Sam)            |
| `SELECT * FROM employee WHERE salary BETWEEN 24000 AND 52000;`      | Rows: employee_id 1 (Alex), 3 (James), 4 (Sam) |
| `SELECT * FROM employee WHERE salary NOT BETWEEN 24000 AND 52000;`  | Row: employee_id 2 (John)                      |
| `SELECT * FROM employee WHERE employee_name IN ('Alex','Sam');`     | Rows: employee_id 1 (Alex), 4 (Sam)            |
| `SELECT * FROM employee WHERE employee_name NOT IN ('Alex','Sam');` | Rows: employee_id 2 (John), 3 (James)          |
| `SELECT * FROM employee WHERE employee_name LIKE 'J%';`             | Rows: employee_id 2 (John), 3 (James)          |
| `SELECT * FROM employee WHERE employee_name NOT LIKE '%a%';`        | Row: employee_id 2 (John)                      |
| `SELECT * FROM employee WHERE allowance IS NULL;`                   | No rows                                        |
| `SELECT * FROM employee WHERE allowance IS NOT NULL;`               | All rows                                       |

## Arithmetic Operations (SQL) — Examples and Results

Assumptions for computed results:

- tax = 2000 for all employees
- hours per employee: [1: 40, 2: 41, 3: 38, 4: 44]

Employee data used for calculations:

| employee_id | employee_name | salary | allowance | tax  | hours |
| ----------- | ------------- | ------ | --------- | ---- | ----- |
| 1           | Alex          | 24000  | 1000      | 2000 | 40    |
| 2           | John          | 55000  | 1000      | 2000 | 41    |
| 3           | James         | 52000  | 1000      | 2000 | 38    |
| 4           | Sam           | 24000  | 1000      | 2000 | 44    |

Operations and results:

| SQL                                                           | Result                                         |
| ------------------------------------------------------------- | ---------------------------------------------- |
| `SELECT salary + allowance FROM employee;`                    | [25000, 56000, 53000, 25000]                   |
| `SELECT * FROM employee WHERE salary + allowance = 25000;`    | Rows: employee_id 1 (Alex), 4 (Sam)            |
| `SELECT salary - tax FROM employee;`                          | [22000, 53000, 50000, 22000]                   |
| `SELECT * FROM employee WHERE salary - tax = 50000;`          | Row: employee_id 3 (James)                     |
| `SELECT * FROM employee WHERE tax * 2 = 4000;`                | All rows (tax is 2000)                         |
| `SELECT allowance / salary * 100 FROM employee;`              | [4.17%, 1.82%, 1.92%, 4.17%]                   |
| `SELECT * FROM employee WHERE allowance / salary * 100 >= 5;` | No rows                                        |
| `SELECT hours % 2 FROM employee;`                             | [0, 1, 0, 0]                                   |
| `SELECT * FROM employee WHERE hours % 2 = 0;`                 | Rows: employee_id 1 (Alex), 3 (James), 4 (Sam) |
