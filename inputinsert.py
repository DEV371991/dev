import mysql.connector

# Establishing a connection to the MySQL server
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Taking input from the user
name = str(input("Enter name: "))
address = str(input("Enter address: "))

# SQL query to insert data into the table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = (name, address)

# Executing the SQL query
cursor.execute(sql, values)

# Committing the changes
conn.commit()

# Closing the cursor and connection
cursor.close()
conn.close()
