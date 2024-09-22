class Book(models.Model):
    _inherit = 'library.book'
    _description = 'Book with author and category'

    author_id = fields.Many2one('res.partner', string='Author', required=True)
    category_id = fields.Many2many('library.book.category', string='Categories')