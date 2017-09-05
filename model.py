from openerp import models, fields, api

class many2manyclass(models.Model):
	_name = 'model.m2m'
	name = fields.Char('Name')
	# Type = fields.Selection([
	# 	('A','type A'),
	# 	('B','type B'),
	# 	('C','type C'),]
	# 	,default='type A')
	Type =fields.Char('type')

class printorder(models.Model):
	_name = 'connect.m2m'
	price = fields.Integer('The price')
	taxe = fields.Integer('The taxe')
	active = fields.Boolean('Active?', default=True)

	print_handle_ids = fields.Many2many('model.m2m')

