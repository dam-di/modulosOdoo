# -*- coding: utf-8 -*-
# from odoo import http


# class Proyectos(http.Controller):
#     @http.route('/proyectos/proyectos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyectos/proyectos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyectos.listing', {
#             'root': '/proyectos/proyectos',
#             'objects': http.request.env['proyectos.proyectos'].search([]),
#         })

#     @http.route('/proyectos/proyectos/objects/<model("proyectos.proyectos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyectos.object', {
#             'object': obj
#         })
