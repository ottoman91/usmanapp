# -*- coding: utf-8 -*-
from openerp import http

# class Usmanapp(http.Controller):
#     @http.route('/usmanapp/usmanapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/usmanapp/usmanapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('usmanapp.listing', {
#             'root': '/usmanapp/usmanapp',
#             'objects': http.request.env['usmanapp.usmanapp'].search([]),
#         })

#     @http.route('/usmanapp/usmanapp/objects/<model("usmanapp.usmanapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('usmanapp.object', {
#             'object': obj
#         })