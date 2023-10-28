import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Northwind.db")

empleado_efectivo = '''
   SELECT FirstName || " " || LastName as Employee, COUNT(*) AS Total
   FROM Orders o 
   JOIN Employees e
   ON e.EmployeeID = o.EmployeeID
   GROUP BY o.EmployeeID
   ORDER BY Total DESC
   LIMIT 10
'''

top_empleados = pd.read_sql_query(empleado_efectivo, conn)
top_empleados.plot(x="Employee", y="Total", kind="bar", figsize=(10,5),legend=False)

plt.title("Empleado con mas ventas")
plt.xlabel("Employee")
plt.ylabel("Total")
plt.xticks(rotation=90)
plt.show()


