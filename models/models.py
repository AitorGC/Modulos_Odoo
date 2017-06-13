# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pieza(models.Model):
	_name = 'gestion.pieza'

	codigoPieza = fields.Char(string="Codigo", size=10, required=True)
	nombrePieza = fields.Char(string="Nombre", size=64, required=True)
	tipoPieza = fields.Char(string="Tipo", size=10, required=True)
	precioPieza	= fields.Float(string="Precio")
	empleadoCoge = fields.Many2one('gestion.empleado', string="Empleado")

class Empleado(models.Model):
	_name = 'gestion.empleado'

	nombre = fields.Char(string="Nombre", size=64, required=True)
	apellidos = fields.Char(string="Apellidos", size=64)
	domicilio = fields.Char(string="Dirección", size=100)
	codigoEmp = fields.One2many('gestion.pieza', 'codigoPieza', string="Piezas a su cargo")