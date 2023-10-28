import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Northwind.db")

query = '''
   SELECT ProductName, SUM(Price * Quantity) as Revenue
   FROM OrderDetails od
   JOIN Products p ON p.ProductID = od.ProductID
   GROUP BY od.ProductID
   ORDER BY Revenue DESC
   LIMIT 10
'''
top_product = pd.read_sql_query(query,conn)

top_product.plot(x="ProductName",y="Revenue", kind="bar", figsize=(10,5),legend=False)

plt.title("10 Productos mas rentables")
plt.xlabel("Productos")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.show()

