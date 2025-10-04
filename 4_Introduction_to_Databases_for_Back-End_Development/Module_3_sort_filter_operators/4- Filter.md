## Filtering (WHERE) — Examples and Results

Employee data used for filters:

| employee_id | employee_name | salary | allowance |
| ----------- | ------------- | ------ | --------- |
| 1           | Alex          | 24000  | 1000      |
| 2           | John          | 55000  | 1000      |
| 3           | James         | 52000  | 1000      |
| 4           | Sam           | 24000  | 1000      |

| SQL                                                                      | Result (employee_id) |
| ------------------------------------------------------------------------ | -------------------- |
| `SELECT * FROM employee WHERE salary > 50000;`                           | [2, 3]               |
| `SELECT * FROM employee WHERE employee_name LIKE 'J%';`                  | [2, 3]               |
| `SELECT * FROM employee WHERE salary BETWEEN 24000 AND 52000;`           | [1, 3, 4]            |
| `SELECT * FROM employee WHERE employee_name IN ('Alex','Sam');`          | [1, 4]               |
| `SELECT * FROM employee WHERE salary = 24000 AND employee_name = 'Sam';` | [4]                  |
| `SELECT * FROM employee WHERE salary = 24000 OR salary = 52000;`         | [1, 3, 4]            |
| `SELECT * FROM employee WHERE NOT (employee_name LIKE '%a%');`           | [2]                  |
| `SELECT * FROM employee WHERE allowance IS NOT NULL;`                    | [1, 2, 3, 4]         |
| `SELECT * FROM employee WHERE salary + allowance >= 53000;`              | [2, 3]               |
