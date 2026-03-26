from odoo import api, fields, models


class EduCourseInstance(models.Model):
    _name = "edu.course.instance"
    _description = "Instances of the Courses"

    name = fields.Char(string="Curso", compute="_compute_instance_name")
    course_id = fields.Many2one(string="Curso", comodel_name="edu.course")
    season_id = fields.Many2one(string="Ciclo lectivo", comodel_name="edu.season")
    period = fields.Selection(
        string="Cuatrimestre",
        selection=[
            ("first", "Primer trimestre"),
            ("second", "Segundo trimestre"),
            ("third", "Tercer trimestre"),
        ],
    )
    class_ids = fields.One2many(
        string="Clases impartidas",
        comodel_name="edu.class",
        inverse_name="course_instance_id",
    )
    student_ids = fields.Many2many(
        string="Alumnos",
        comodel_name="edu.student",
        relation="course_instance_student_rel",
        column1="course_instance_id",
        column2="student_id",
    )
    student_history_ids = fields.One2many(
        string="Acta de notas",
        comodel_name="edu.student.history",
        inverse_name="course_instance_id",
    )

    @api.depends("course_id.name", "season_id.name", "period")
    def _compute_instance_name(self):
        for rec in self:
            if rec.course_id and rec.season_id and rec.period:
                rec.name = f"{rec.course_id.name} - {rec.season_id.name}"
            else:
                rec.name = "Nueva Instancia"
