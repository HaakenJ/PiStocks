import mysql.connector

# This is the schema to set up the proper database and 
# tables for the application.

#try:
#    db = mysql.connector.connect(
#        host='localhost',
#        user='root',
#        password='kramer',
#        database='stock_db'
#    )
#except:
db = mysql.connector.connect(
    host='localhost',
    user='kramer',
    password='kramer',
    database='stock_ db'
)

cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS stock_db;')
cursor.execute('USE stock_db;')
cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_data (
	id INT NOT NULL AUTO_INCREMENT,
	entryDate DATETIME,
    symbol VARCHAR(10) NOT NULL,
    price DOUBLE NOT NULL,
    PRIMARY KEY (id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS portfolio (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    cost DOUBLE NOT NULL,
    shares INT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS prior_day (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    entryDate DATETIME,
    value DOUBLE NOT NULL
);
""")

db.commit()
print('Database and tables successfully created. (or already existed)')
