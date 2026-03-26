from odoo import fields, models


class EduStudent(models.Model):
    _name = "edu.student"
    _description = "Students"

    name = fields.Char(string="Nombre completo y apellido")
    photo = fields.Binary(string="Foto")
    dni = fields.Integer(string="Número de documento")
    birthday = fields.Date(string="Fecha de nacimiento")
    living_place = fields.Char(string="Domicilio")
    phone = fields.Integer(string="Número de teléfono")
    max_educative_level = fields.Selection(
        string="Máximo nivel edicativo",
        selection=[
            ("fin_uni", "Universitario/Terciario completo"),
            ("none_fin_uni", "Universitario/Terciario incompleto"),
            ("fin_high", "Secundario completo"),
            ("none_fin_high", "Secundaria incompleta"),
            ("fin_pri", "Primaria completa"),
            ("none_fin_pri", "Primaria incompleta"),
        ],
    )
    student_history_ids = fields.One2many(
        string="Cursos realizados",
        comodel_name="edu.student.history",
        inverse_name="student_id",
    )
    class_assistance_ids = fields.One2many(
        string="Asistencias a las clases",
        comodel_name="edu.class.assistance",
        inverse_name="student_id",
    )
