# -*- coding: utf-8 -*-

from odoo import models, fields

class Curso(models.Model):
    _name = 'sistema.curso'
    _rec_name = 'nombres_cursos'
    _description = 'Lista con los cursos del colegio'

    
    cod_curso = fields.Char('Número Curso', required=True)
    número_sala = fields.Char('Número Sala ', required=True)
    Cantidad_alumnos = fields.Integer('cantidad Alumnos', required=True)
    id_profesor = fields.integer(string='id profesor', required=True)
    
