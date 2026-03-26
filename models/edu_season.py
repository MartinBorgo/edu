from odoo import fields, models


class EduSeason(models.Model):
    _name = "edu.season"
    _description = "Seasons"

    name = fields.Char(string="Ciclo lectivo")
    course_instance_ids = fields.One2many(
        string="Cursos impartidos",
        comodel_name="edu.course.instance",
        reverse_name="season_id",
    )
