from odoo import fields, models


class EduAttendanceLineWizard(models.TransientModel):
    _name = "edu.attendance.line.wizard"
    _description = "Wizard which represent the asistance lines in the real model"

    wizard_id = fields.Many2one("edu.attendance.wizard")
    student_id = fields.Many2one(string="Alumno", comodel_name="edu.student")
    assistance = fields.Boolean(string="Presente")
