from odoo import api, fields, models


class EduAttendanceWizard(models.TransientModel):
    _name = "edu.attendance.wizard"
    _description = "Wizards which generate assistance records"

    course_instance_id = fields.Many2one(
        string="Curso",
        comodel_name="edu.course.instance"
    )
    date = fields.Date(string="Fecha de la clase", default=fields.Date.today)
    lines = fields.One2many(
        string="Asistencias",
        comodel_name="edu.attendance.line.wizard",
        inverse_name="wizard_id"
    )

    @api.model
    def default_get(self, field_list):
        res = super(EduAttendanceWizard, self).default_get(field_list)
        instance_id = res.get("course_instance_id")
        if instance_id:
            lines = []
            instance = self.env["edu.course.instance"].browse(instance_id)
            for student in instance.student_ids:
                lines.append((0, 0, {"student_id": student.id, "assistance": False}))
            res.update({"course_instance_id": instance_id, "line_ids": lines})
        return res

    def action_confirm(self):
        new_class = self.env["edu.class"].create(
            {
                "date": self.date,
                "course_instance_id": self.course_instance_id.id,
            }
        )

        for line in self.line_ids:
            self.env["edu.class.assistance"].create(
                {
                    "class_id": new_class.id,
                    "student_id": line.student_id.id,
                    "assistance": line.assistance,
                }
            )
        return {"type": "ir.actions.act_window_close"}
