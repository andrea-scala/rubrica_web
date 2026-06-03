from werkzeug.security import generate_password_hash
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

conn = pymysql.connect(
    host     = os.getenv('HOST'),
    port     = int(os.getenv('PORT')),
    database = os.getenv('DB'),
    user     = os.getenv('USERNAME'),
    password = os.getenv('PASSWORD')
)
cursor = conn.cursor()
cursor.execute(
    "INSERT INTO utenti (username, password_hash) VALUES (%s, %s)",
    ('admin', generate_password_hash('admin'))
)
conn.commit()
cursor.close()
conn.close()
print("Utente admin creato correttamente")
