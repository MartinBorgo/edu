from odoo import fields, models


class EduCourseCommission(models.Model):
    _name = "edu.course.commission"
    _descripción = "Course commissions"

    name = fields.Char(string="Comisión")
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
    course_instance_id = fields.Many2one(
        string="Curso",
        comodel_name="edu.course.instance"
    )
    class_ids = fields.One2many(
        string="Clases",
        comodel_name="edu.class",
        inverse_name="commission_id"
    )
    student_ids = fields.Many2many(
        string="Alumnos",
        comodel_name="edu.student",
        relation="edu_commission_student_rel",
        column1="commission_id",
        column2="student_id"
    )
