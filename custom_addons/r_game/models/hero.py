from odoo import api, fields, models


class Hero(models.Model):
    _name = 'r.hero'
    _description = 'Hero'

    name = fields.Char(
        string='name',
        required=True,
        help='fill hero name'
    )

    description = fields.Text(
        string='description'
    )

    active = fields.Boolean(
        string='active',
        default=True
    )
