from odoo import fields, models

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'

    name = fields.Char(string='Name', required=True, unique=True)