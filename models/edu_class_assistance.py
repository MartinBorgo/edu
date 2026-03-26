from odoo import fields, models


class EduClassAssistance(models.Model):
    _name = "edu.class.assistance"
    _description = "Class Assistance"

    class_id = fields.Many2one(string="Clase", comodel_name="edu.class")
    student_id = fields.Many2one(string="Alumno", comodel_name="edu.student")
    assistance = fields.Boolean(string="Presente", default=False)
