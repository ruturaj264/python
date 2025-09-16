import pymysql
import random
import string
from datetime import date, timedelta

# ---------- RDS Connection ----------
host = "bank-rds.cz6aacak4fmf.ap-south-1.rds.amazonaws.com"
port = 3306
user = "bank_rds_admin"
password = "19A1a1krev0"
database = "bankdb"

conn = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    port=port,
    autocommit=True
)
cursor = conn.cursor()

# ---------- Helper Functions ----------
def random_string(length=10):
    
    if _ % 1000 == 0:
        return None
        
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_id():
    
    if _ % 900 == 0:
        return None
        
    return random.randint(1, 10000)

def random_amount():
    
    if _ % 800 == 0:
        return None
    
    return round(random.uniform(-1000, 5000), 2)

def random_status():
    return random.choice(['COMPLETED', 'PENDING', 'FAILED', 'CANCELLED', ' CoMPLETED', ' PENdING', ' FAILeD', ' CAnCELLED', None])

def random_description():
    return random.choice(['purchase', 'refund', 'transfer', 'payment', 'xyz', 'abc', 'lorem', 'test', None, ' purchase', ' refund', ' transfer'])

def random_payment_type():
    return random.choice(['CARD', 'CASH', 'UPI', 'BANK_TRANSFER', ' card', ' CASH', ' upi', ' Bank_TRANSFER', None])

def random_currency():
    return random.choice(['INR', 'inr', 'Inr', 'INr', None])

def random_location():
    return random.choice(['Mumbai', ' Delhi', 'Bangalore', ' Chennai', ' Hyderabad', 'mumbai', ' delhi', 'bangalore', ' chennai', 'hyderabad', None])

def random_notes():
    return random.choice(['note', 'info', 'detail', 'misc', 'xyz', 'abc', None])

# ---------- Insert Transactions ----------
num_rows = 500000  # ~50 MB/day
batch_size = 25000
# yesterday = (date.today()).strftime('%Y-%m-%d')
yesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')

insert_query = """
INSERT INTO transactions
(transaction_id, customer_id, amount, transaction_date, status, description,
 merchant_id, payment_type, currency, location, notes)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for start in range(0, num_rows, batch_size):
    batch_records = []
    for _ in range(min(batch_size, num_rows - start)):
        transaction_id = random_string(12)
        customer_id = random_id()
        amount = random_amount()
        status = random_status()
        description = random_description()
        merchant_id = random.randint(1, 200)
        payment_type = random_payment_type()
        currency = random_currency()
        location = random_location()
        notes = random_notes()
        batch_records.append((transaction_id, customer_id, amount, yesterday, status, description,
                              merchant_id, payment_type, currency, location, notes))
    cursor.executemany(insert_query, batch_records)
    print(f"Inserted batch {start // batch_size + 1} ({len(batch_records)} rows)")

print(f"Inserted total {num_rows} messy transactions for {yesterday}")

# ---------- Close Connection ----------
cursor.close()
conn.close()
