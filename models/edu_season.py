from odoo import fields, models


class EduSeason(models.Model):
    _name = "edu.season"
    _description = "Seasons"

    name = fields.Char(
        string="Ciclo lectivo",
        required=True
    )
    course_instance_ids = fields.One2many(
        string="Cursos impartidos",
        comodel_name="edu.course.instance",
        inverse_name="season_id"
    )
