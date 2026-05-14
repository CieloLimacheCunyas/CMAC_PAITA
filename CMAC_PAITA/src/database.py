import mysql.connector

from dotenv import load_dotenv

import os

# =========================
# LOAD ENV
# =========================

load_dotenv()

# =========================
# MYSQL CONNECTION
# =========================

db = mysql.connector.connect(

    host=os.getenv(
        "DB_HOST"
    ),

    user=os.getenv(
        "DB_USER"
    ),

    password=os.getenv(
        "DB_PASSWORD"
    ),

    database=os.getenv(
        "DB_NAME"
    )

)

# =========================
# CURSOR
# =========================

cursor = db.cursor(
    dictionary=True
)