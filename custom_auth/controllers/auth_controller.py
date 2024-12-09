import jwt
import datetime
from odoo import http
from odoo.http import request, Response

SECRET_KEY="secret_key"

class AuthController(http.Controller):
    @http.route("/api/signin", type="json", auth="none", methods=["POST"])
    def signin(self, **kwargs):
        try:
            username = kwargs.get("username")
            password = kwargs.get("password")

            if not username:
                throw ValueError("Username required")

            if not password:
                throw ValueError("Password required")

            user = request.env["res.users"].sudo().search(["login", "=", username])

            if not user or not user._check_credentials(password):
                raise ValueError("Invalid username or password")

            payload = {
                "userId": user.id,
                "lgin": user.login,
                "iat": datetime.datetime.utcnow(),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            }

            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            return {
                "status": "error",
                "message": "Authentication successful",
                "token": token
            }

        except ValueError as e:
            return {
                "status": "error",
                "message": str(e)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": "An unexpected error occurred: " + str(e)
            }
