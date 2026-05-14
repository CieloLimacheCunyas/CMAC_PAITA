# =========================
# src/auth.py
# =========================

from flask import (

    Blueprint,
    render_template,
    request,
    redirect,
    flash

)

from src.user_model import (

    create_user,
    login_user

)

# =========================
# BLUEPRINT
# =========================

auth_bp = Blueprint(

    'auth',

    __name__

)

# =========================
# LOGIN PAGE
# =========================

@auth_bp.route('/')
def login_page():

    return render_template(
        'login.html'
    )

# =========================
# REGISTER PAGE
# =========================

@auth_bp.route('/register-page')
def register_page():

    return render_template(
        'register.html'
    )

# =========================
# REGISTER
# =========================

@auth_bp.route(

    '/register',

    methods=['POST']

)
def register():

    dni = request.form['dni']

    nombre = request.form['nombre']

    tarjeta = request.form['tarjeta']

    password = request.form['password']

    pin = request.form['pin']

    create_user(

        dni,
        nombre,
        tarjeta,
        password,
        pin

    )

    flash(
        "USUARIO REGISTRADO"
    )

    return redirect('/')

# =========================
# LOGIN
# =========================

@auth_bp.route(

    '/login',

    methods=['POST']

)
def login():

    dni = request.form['dni']

    password = request.form['password']

    user = login_user(

        dni,
        password

    )

    if user:

        return f"""

        <h1>
        Bienvenido {user['nombre']}
        </h1>

        """

    else:

        return """

        <h1>
        DATOS INCORRECTOS
        </h1>

        """