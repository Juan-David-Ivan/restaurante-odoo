# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Plato(models.Model):
    _name = 'restaurante.plato'
    _description = 'Plato de comida de un restaurante'
    _rec_name = 'nombrePlato'

    #Atriburos
    nombrePlato = fields.Char(string='Nombre del plato', required=True)
    tipoPlato = fields.Char(string='Tipo de plato', required=True)
    precioPlato = fields.Char(string='Precio del plato', required=True)

    #Relacion con ingredientes y categoria
    ingrediente_ids = fields.Many2many('restaurante.ingrediente','plato_id', string='Ingrediente')
    categoria_ids = fields.One2many('restaurante.categoria','plato_id', string='Categoria')

        
class Ingrediente(models.Model):
    _name = 'restaurante.ingrediente'
    _description = 'Ingrediente de un plato'
    _rec_name = 'nombreIngrediente'

    #Atributos
    nombreIngrediente = fields.Char(string='Nombre del ingrediente', required=True)
    cantidadIngrediente = fields.Integer(string='Cantidad de ese ingrediente', required=True)

    #Relación con platos
    plato_ids = fields.Many2many('restaurante.plato','ingrediente_id', string='Plato')

class Categoria(models.Model):
    _name = 'restaurante.categoria'
    _description = 'Categoria de un plato'
    _rec_name = 'nombreCategoria'

    #Atributos
    nombreCategoria = fields.Char(string='Nombre de la categoria', required=True)

    #Relacion con platos
    plato_id = fields.Many2one('restaurante.plato',string='Plato')






# class restaurante(models.Model):
#     _name = 'restaurante.restaurante'
#     _description = 'restaurante.restaurante'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

