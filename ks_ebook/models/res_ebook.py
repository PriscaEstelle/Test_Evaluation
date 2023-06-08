# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

 class ResEbook(models.Model):
     _name = 'res.ebook'
     _description = 'resebook'

     reference = fields.Char(string='ID',readonly=True,readonly=True )
     title = fields.Char(string='Title', required=True)
     description = fields.Html(string='Description')
     file  = fields.Binary(string='Field Label', attachment=True)  
     file_name  = fields.Char(string='Folder')
     banner  = fields.Binary(string='Banner', attachment=True)
     added_by = fields.Many2one('res.user', required=True)
     creation_date = fields.Date(string='Creation_date', default=date.today(), required=True)
     state = fields.Selection(
         selection=[('disorganized', 'Disorganized'),
          ('published', 'Published'),
          ('canceled', 'Canceled')],
            default='new')

    def desorganized(self):
    	self.state = 'desorganized'

    def published(self):
    	self.state = 'published'

    def canceled(self):
    	self.state = 'canceled'		