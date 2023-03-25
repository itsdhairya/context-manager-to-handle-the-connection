import mysql.connector
import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, filename='sql.log')

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
            logging.error("An error occurred: {}".format(exc_val))
        else:
            self.conn.commit()
        self.cursor.close()
        self.conn.close()

# Use the context manager to execute queries
with Database(host="localhost", user="username", password="password", database="mydatabase") as cursor:
    # Create a table
    cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")

    # Insert data into the table
    sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
    val = ("John Doe", "johndoe@example.com")
    cursor.execute(sql, val)

    # Execute a SELECT query
    cursor.execute("SELECT * FROM customers")

    # Fetch the results and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Update data in the table
    sql = "UPDATE customers SET email = %s WHERE name = %s"
    val = ("newemail@example.com", "John Doe")
    cursor.execute(sql, val)

    # Delete data from the table
    sql = "DELETE FROM customers WHERE name = %s"
    val = ("John Doe",)
    cursor.execute(sql, val)

