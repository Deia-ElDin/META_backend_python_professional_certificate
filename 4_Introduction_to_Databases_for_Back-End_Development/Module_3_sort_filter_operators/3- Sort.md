## Sorting (ORDER BY) — Examples and Results

Employee data used for sorting:

| employee_id | employee_name | salary | allowance |
| ----------- | ------------- | ------ | --------- |
| 1           | Alex          | 24000  | 1000      |
| 2           | John          | 55000  | 1000      |
| 3           | James         | 52000  | 1000      |
| 4           | Sam           | 24000  | 1000      |

| SQL                                                                         | Result order (employee_id) |
| --------------------------------------------------------------------------- | -------------------------- |
| `SELECT * FROM employee ORDER BY salary ASC;`                               | [1, 4, 3, 2]               |
| `SELECT * FROM employee ORDER BY salary DESC;`                              | [2, 3, 1, 4]               |
| `SELECT * FROM employee ORDER BY employee_name ASC;`                        | [1, 3, 2, 4]               |
| `SELECT * FROM employee ORDER BY salary ASC, employee_name ASC;`            | [1, 4, 3, 2]               |
| `SELECT * FROM employee ORDER BY salary ASC, employee_name DESC;`           | [4, 1, 3, 2]               |
| `SELECT * FROM employee ORDER BY salary + allowance DESC, employee_id ASC;` | [2, 3, 1, 4]               |
