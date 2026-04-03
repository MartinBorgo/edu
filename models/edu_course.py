from odoo import fields, models


class EduCourse(models.Model):
    _name = "edu.course"
    _description = "Courses"

    name = fields.Char(string="Nombre del curso")
    content = fields.Html(string="Programa de contenidos")
    class_days = fields.Selection(
        string="Día de cursada",
        selection=[
            ("mon", "Lunes"),
            ("tue", "Martes"),
            ("wed", "Miercoles"),
            ("thu", "Jueves"),
            ("fri", "Viernes"),
        ],
    )
    start_hour = fields.Float(string="Hora de inicio")
    end_hour = fields.Float(string="Hora de finalización")
    student_limit = fields.Integer(string="Cupo de estudiantes", default=15)
    teacher_ids = fields.Many2many(
        string="Capacitador",
        comodel_name="res.users",
        relation="course_teacher_rel",
        column1="course_id",
        column2="teacher_id",
    )
    course_instance_ids = fields.One2many(
        string="Instancias impartidas",
        comodel_name="edu.course.instance",
        inverse_name="course_id",
    )
