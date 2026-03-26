from odoo import api, fields, models
from odoo.tools import format_date


class EduClass(models.Model):
    _name = "edu.class"
    _description = "Courses Classes"

    name = fields.Char(compute="_compute_class_name")
    date = fields.Date(string="Fecha", default=fields.Date.today)
    course_instance_id = fields.Many2one(
        string="Curso",
        comodel_name="edu.course.instance"
    )
    assistance_ids = fields.One2many(
        string="Asistencias",
        comodel_name="edu.class.assistance",
        inverse_name="class_id"
    )

    @api.depends("date", "course_instance_id")
    def _compute_class_name(self):
        for rec in self:
            formated_date = format_date(
                self.env, self.date, lang_code=self.env.user.lang
            )
            rec.name = f"Clase {formated_date}"
