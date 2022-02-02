# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyectos(models.Model):
#     _name = 'proyectos.proyectos'
#     _description = 'proyectos.proyectos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import model, fields, api

class departamento(models.Model):
    _name = 'proyectos.departamento'
    _description = 'Define los atributos de un departamento'

    nombreDepartamento= fields.Char(string='Nombre departamento', required=True)

class empleado(models.Model):
    _name = 'proyectos.empleado'
    _description = 'Atributos para un empleado'

    dniEmpleado = fields.Char(string='DNI', requiered=True)
    nombreEmpleado = fields.Char(string='Nombre', requiered=True)
    fechaNacimiento = fields.Date(string='Fecha nacimiento', requiered=True, default = fields.date.today)
    direccionEmpleado = fields.Char(string='Dirección', requiered=True)
    telefonoEmpleado = fields.Char(string='Telefono', requiered=True)
    edad = fields.Integer('Edad', compute='getEdad')

    @api.depends('fechaNacimiento')
    def getEdad(self):
        for empleado in self:
            empleado.edad = 0

class proyecto(models.Model):
    _name = 'proyectos.proyecto'
    _description = 'Atributos de un proyecto'

class empleado_proyecto(models.Model):
    _name = 'proyectos.empleado_proyecto'
    _description = 'Modelo relacional empleado - proyecto'
