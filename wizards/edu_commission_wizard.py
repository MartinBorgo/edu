from odoo import api ,fields, models
from odoo.exceptions import UserError


class EduCommissionWizard(models.TransientModel):
    _name = "edu.commission.wizard"
    _description = "Wizard which create course commissions"

    name = fields.Char(
        string="Comisión",
        required=True
    )
    class_days = fields.Selection(
        string="Día de cursada",
        selection=[
            ("mon", "Lunes"),
            ("tue", "Martes"),
            ("wed", "Miercoles"),
            ("thu", "Jueves"),
            ("fri", "Viernes"),
        ],
        required=True
    )
    start_hour = fields.Float(
        string="Hora de inicio de clases",
        required=True
    )
    end_hour = fields.Float(
        string="Hora de finalización de clases",
        required=True
    )
    course_instance_id = fields.Many2one(
        string="Curso",
        comodel_name="edu.course.instance"
    )
    lines = fields.One2many(
        string="Alumnos",
        comodel_name="edu.commission.line.wizard",
        inverse_name="wizard_id"
    )

    @api.model
    def default_get(self, field_list):
        res = super().default_get(field_list)
        active_id = self.env.context.get("active_id")

        if active_id:
            course = self.env["edu.course.instance"].browse(active_id)
            assigned_student = course.commission_ids.mapped('student_ids').ids or []
            lines = [
                (0, 0, {"student_id": student.id, "is_part": False})
                for student in course.student_ids
                if student.id not in assigned_student
            ]
            res.update({"course_instance_id": course.id, "lines": lines})

        return res

    def action_confirm(self):
        selected_students = self.lines.filtered(lambda l: l.is_part).mapped('student_id')
        if not selected_students:
            raise UserError("Debe seleccionar al menos un alumno para poder crear la comisión.")

        if self.start_hour >= self.end_hour:
            raise UserError("La hora de inicio de clases no puede ser mayor o igual a la hora de finalización.")

        self.env["edu.course.commission"].create({
            "name": self.name,
            "class_days": self.class_days,
            "start_hour": self.start_hour,
            "end_hour": self.end_hour,
            "course_instance_id": self.course_instance_id.id,
            "student_ids": [(6, 0, selected_students.ids)],
        })

        return {"type": "ir.actions.act_window_close"}
