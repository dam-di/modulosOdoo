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
from odoo import models, fields, api

class departamento(models.Model):
    _name = 'proyectos.departamento'
    _description = 'Define los atributos de un departamento'
    
    nombreDepartamento= fields.Char(string='Nombre departamento', required=True)
    
    #Relaciones entre tablas
    #Comentario de prueba
    empleado_id = fields.One2many('proyectos.empleado','departamento_id' ,string='Departamento')

class empleado(models.Model):
    _name = 'proyectos.empleado'
    _description = 'Atributos para un empleado'
    #atributos
    dniEmpleado = fields.Char(string='DNI', requiered=True)
    nombreEmpleado = fields.Char(string='Nombre', requiered=True)
    fechaNacimiento = fields.Date(string='Fecha nacimiento', requiered=True, default = fields.date.today())
    direccionEmpleado = fields.Char(string='Dirección', requiered=True)
    telefonoEmpleado = fields.Char(string='Telefono', requiered=True)
    edad = fields.Integer('Edad', compute='getEdad')

    @api.depends('fechaNacimiento')
    def getEdad(self):
        for empleado in self:
            empleado.edad = 0
    
    #relaciones entre tablas
    departamento_id = fields.Many2one('proyectos.departamento', string='Empleados')
    proyecto_ids = fields.Many2many('proyectos.proyecto', string='Proyectos')

class proyecto(models.Model):
    _name = 'proyectos.proyecto'
    _description = 'Atributos de un proyecto'
    
    nombreProyecto = fields.Char(string='Nombre proyecto', requiered=True)
    tipoProyecto = fields.Selection(string='Tipo de proyecto', selection=[('f','Front-End'),('b','Back-End')], requiered=True, help='Indica el tipo de proyecto')
    ciudadProyecto = fields.Char(string='Ciudad')
    decripcionProyecto = fields.Text(string='Descripcion del proyecto', help='Indica una descripción del proyecto')

    #Relación entre tablas
    empleado_ids = fields.Many2many('proyectos.empleado', string='Empleados')






#class empleado_proyecto(models.Model):
#   _name = 'proyectos.empleado_proyecto'
#    _description = 'Modelo relacional empleado - proyecto'
#
#    empleado_ids = fields.Many2many('proyectos.empleado','empleado_id')