from flask import Flask

from src.auth import auth_bp

from dotenv import load_dotenv

from asgiref.wsgi import WsgiToAsgi

import os

# =========================
# LOAD ENV
# =========================

load_dotenv()

# =========================
# FLASK APP
# =========================

flask_app = Flask(

    __name__,

    template_folder='html',

    static_folder=''

)

# =========================
# SECRET KEY
# =========================

flask_app.secret_key = os.getenv(
    "SECRET_KEY"
)

# =========================
# REGISTER BLUEPRINT
# =========================

flask_app.register_blueprint(
    auth_bp
)

# =========================
# ASGI APP
# =========================

app = WsgiToAsgi(
    flask_app
)