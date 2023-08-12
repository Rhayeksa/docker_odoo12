# -*- coding: utf-8 -*-
from odoo import http

# class RGame(http.Controller):
#     @http.route('/r_game/r_game/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/r_game/r_game/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('r_game.listing', {
#             'root': '/r_game/r_game',
#             'objects': http.request.env['r_game.r_game'].search([]),
#         })

#     @http.route('/r_game/r_game/objects/<model("r_game.r_game"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('r_game.object', {
#             'object': obj
#         })
