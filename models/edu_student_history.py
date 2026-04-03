from odoo import fields, models


class EduStudentHistory(models.Model):
    _name = "edu.student.history"
    _description = "Student History"

    course_instance_id = fields.Many2one(
        string="Curso", comodel_name="edu.course.instance"
    )
    student_id = fields.Many2one(string="Estudiante", comodel_name="edu.student")
    student_state = fields.Selection(
        string="Estado",
        selection=[
            ("pass", "Egresado"),
            ("not_pass", "No egresado"),
            ("attending", "Cursando"),
            ("give_up", "Abandono"),
        ],
        default="attending",
    )
