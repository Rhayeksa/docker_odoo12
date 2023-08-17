# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Order(models.Model):
    _name = 'rds_market.order'
    _description = 'rds market order model'

    code = fields.Char(
        string='code',
        size=45,
        required=True,
        help='Order Code',
    )

    quantity = fields.Integer(
        string='quantity',
        required=True,
        help='Order Quantity',
    )

    product_id = fields.Many2one(
        comodel_name='rds_market.product',
        string='product_id',
        required=True,
        help='Product Id from model product',
    )

    customer_id = fields.Many2one(
        comodel_name='rds_market.customer',
        string='customer_id',
        required=True,
        help='Customer Id from model customer',
    )
