## DISTINCT (remove duplicates) — Examples and Results

Employee data used:

| employee_id | employee_name | salary | allowance |
| ----------- | ------------- | ------ | --------- |
| 1           | Alex          | 24000  | 1000      |
| 2           | John          | 55000  | 1000      |
| 3           | James         | 52000  | 1000      |
| 4           | Sam           | 24000  | 1000      |

| SQL                                                | Result                                        |
| -------------------------------------------------- | --------------------------------------------- |
| `SELECT DISTINCT salary FROM employee;`            | [24000, 52000, 55000]                         |
| `SELECT DISTINCT allowance FROM employee;`         | [1000]                                        |
| `SELECT DISTINCT employee_name FROM employee;`     | [Alex, John, James, Sam]                      |
| `SELECT DISTINCT salary, allowance FROM employee;` | [(24000, 1000), (52000, 1000), (55000, 1000)] |
| `SELECT COUNT(DISTINCT salary) FROM employee;`     | 3                                             |
