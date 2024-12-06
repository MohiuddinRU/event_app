# -*- coding: utf-8 -*-
# from odoo import http


# class CustomEvent(http.Controller):
#     @http.route('/custom_event/custom_event', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_event/custom_event/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_event.listing', {
#             'root': '/custom_event/custom_event',
#             'objects': http.request.env['custom_event.custom_event'].search([]),
#         })

#     @http.route('/custom_event/custom_event/objects/<model("custom_event.custom_event"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_event.object', {
#             'object': obj
#         })

