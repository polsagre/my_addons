# -*- coding: utf-8 -*-
# from odoo import http


# class MyAddons/modulo1(http.Controller):
#     @http.route('/my_addons/modulo1/my_addons/modulo1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_addons/modulo1/my_addons/modulo1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_addons/modulo1.listing', {
#             'root': '/my_addons/modulo1/my_addons/modulo1',
#             'objects': http.request.env['my_addons/modulo1.my_addons/modulo1'].search([]),
#         })

#     @http.route('/my_addons/modulo1/my_addons/modulo1/objects/<model("my_addons/modulo1.my_addons/modulo1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_addons/modulo1.object', {
#             'object': obj
#         })
