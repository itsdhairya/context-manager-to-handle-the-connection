# context-manager-to-handle-the-connection
This code defines a Database class that serves as a context manager for handling the connection and cursor objects. The __enter__() method establishes a connection to the database and returns the cursor object. The __exit__() method commits changes to the database if no exceptions were raised, or rolls back the transaction if an exception occurred. The code also includes error handling and logging, so any errors are logged to a file named sql.log.

The main part of the code uses the with statement to execute queries using the Database context manager. The code creates a customers table, inserts a new record, retrieves all the records, updates a record, and deletes a record.
