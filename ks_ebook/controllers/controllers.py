# -*- coding: utf-8 -*-
# from odoo import http


# class KsEbook(http.Controller):
#     @http.route('/ks_ebook/ks_ebook', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ks_ebook/ks_ebook/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ks_ebook.listing', {
#             'root': '/ks_ebook/ks_ebook',
#             'objects': http.request.env['ks_ebook.ks_ebook'].search([]),
#         })

#     @http.route('/ks_ebook/ks_ebook/objects/<model("ks_ebook.ks_ebook"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ks_ebook.object', {
#             'object': obj
#         })
