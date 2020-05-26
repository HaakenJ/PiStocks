import mysql.connector

# This is where the seeds for your portfolio are set up.
# Add whatever stocks you own into the parameters tuple 
# along with the number of shares owned and the original
# purchase cost.

db = mysql.connector.connect(
    host='localhost',
    user='kramer',
    password='kramer',
    database='stock_db'
)

cursor = db.cursor()

parameters = [
    ('ALK', 26.46, 14),
    ('PENN', 16.15, 12),
    ('MSFT', 159.00, 2),
    ('MVIS', 1.02, 423),
    ('VTIQ', 28.75, 8),
    ('ERI', 28, 10)
]
query = 'INSERT INTO portfolio (symbol, cost, shares) VALUES (%s, %s, %s)'

cursor.executemany(query, parameters)

db.commit()
print(cursor.rowcount, 'record(s) inserted.')
