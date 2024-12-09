#pip install pyjwt
import jwt
import datetime
from odoo import http
from odoo.http import request, Response
import json
import odoo
import odoo.modules.registry
from odoo.tools.translate import _


SECRET_KEY = "secret_key"


class AuthController(http.Controller):
    @http.route("/api/signin", type="http", auth="public", methods=["POST"], csrf=False)
    def signin(self, **kwargs):
        try:
            username = request.httprequest.json.get("username")
            password = request.httprequest.json.get("password")

            if not username:
                raise ValueError("Username required")

            if not password:
                raise ValueError("Password required")

            user = request.env["res.users"].sudo().search([("login", "=", username)])
            values = {}

            uid = request.session.authenticate(request.db, username, password)
            if not uid:
                raise ValueError(_('Wrong login/password'))

            request.params["login_success"] = True
            user = user.with_user(1)
            payload = {
                "userId": user.id,
                "lgin": user.login,
                "iat": datetime.datetime.utcnow(),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            }

            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

            response = {
                "status": "success",
                "message": "Authentication successful",
                "token": token,
            }
            return json.dumps(response, default=str)

        except odoo.exceptions.AccessDenied as e:
                if e.args == odoo.exceptions.AccessDenied().args:
                    values["error"] = _("Wrong login/password")
                else:
                    values["error"] = e.args[0]
                raise Exception(values['error'])

        except ValueError as e:
            return json.dumps({"status": "error", "message": str(e)}, default=str)
        except Exception as e:
            return json.dumps(
                {
                    "status": "error",
                    "message": "An unexpected error occurred: " + str(e),
                },
                default=str,
            )
