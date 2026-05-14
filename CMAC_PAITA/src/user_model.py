# =========================
# src/user_model.py
# =========================

from src.database import (
    db,
    cursor
)

import bcrypt

# =========================
# CREATE USER
# =========================

def create_user(

    dni,
    nombre,
    tarjeta,
    password,
    pin

):

    # =========================
    # ENCRYPT PASSWORD
    # =========================

    password_encrypt = bcrypt.hashpw(

        password.encode('utf-8'),

        bcrypt.gensalt()

    ).decode('utf-8')

    # =========================
    # ENCRYPT PIN
    # =========================

    pin_encrypt = bcrypt.hashpw(

        pin.encode('utf-8'),

        bcrypt.gensalt()

    ).decode('utf-8')

    # =========================
    # SQL
    # =========================

    sql = """
    INSERT INTO usuarios(

        dni,
        nombre,
        tarjeta,
        password,
        pin

    )

    VALUES(%s,%s,%s,%s,%s)
    """

    values = (

        dni,
        nombre,
        tarjeta,
        password_encrypt,
        pin_encrypt

    )

    cursor.execute(
        sql,
        values
    )

    db.commit()

# =========================
# LOGIN USER
# =========================

def login_user(

    dni,
    password

):

    sql = """
    SELECT * FROM usuarios
    WHERE dni=%s
    """

    values = (
        dni,
    )

    cursor.execute(
        sql,
        values
    )

    user = cursor.fetchone()

    if user:

        password_db = user['password']

        if bcrypt.checkpw(

            password.encode('utf-8'),

            password_db.encode('utf-8')

        ):

            return user

    return None