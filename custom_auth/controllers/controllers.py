# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAuth(http.Controller):
#     @http.route('/custom_auth/custom_auth', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_auth/custom_auth/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_auth.listing', {
#             'root': '/custom_auth/custom_auth',
#             'objects': http.request.env['custom_auth.custom_auth'].search([]),
#         })

#     @http.route('/custom_auth/custom_auth/objects/<model("custom_auth.custom_auth"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_auth.object', {
#             'object': obj
#         })

