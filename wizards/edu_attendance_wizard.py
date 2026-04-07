from odoo import api, fields, models


class EduAttendanceWizard(models.TransientModel):
    _name = "edu.attendance.wizard"
    _description = "Wizards which generate assistance records"

    course_instance_id = fields.Many2one(
        string="Curso",
        comodel_name="edu.course.instance"
    )
    commission_id = fields.Many2one(
        string="Comisión",
        comodel_name="edu.course.commission",
        domain="[('course_instance_id', '=', course_instance_id)]",
        required=True
    )
    date = fields.Date(string="Fecha de la clase", default=fields.Date.today)
    lines = fields.One2many(
        string="Asistencias",
        comodel_name="edu.attendance.line.wizard",
        inverse_name="wizard_id",
    )

    @api.model
    def default_get(self, field_list):
        res = super().default_get(field_list)
        active_id = self.env.context.get("active_id")

        if active_id:
            # course = self.env["edu.course.instance"].browse(active_id)
            # lines = [
            #     (0, 0, {"student_id": student.id, "assistance": True})
            #     for student in course.student_ids
            # ]
            res.update({"course_instance_id": active_id})

        return res

    @api.onchange("commission_id")
    def _onchange_commission_id(self):
        if not self.commission_id:
            self.lines = [(5, 0, 0)]
            return

        lines = [
            (0, 0, {"student_id": student.id, "assistance": True})
            for student in self.commission_id.student_ids
        ]

        self.lines = [(5, 0, 0)] + lines

    def action_confirm(self):
        self.ensure_one()

        new_class = self.env["edu.class"].create({
            "date": self.date,
            "course_instance_id": self.course_instance_id.id,
            "commission_id": self.commission_id.id
        })

        assistances = []
        for line in self.lines:
            assistances.append({
                "class_id": new_class.id,
                "student_id": line.student_id.id,
                "assistance": line.assistance
            })

        if assistances:
            self.env["edu.class.assistance"].create(assistances)

        return {"type": "ir.actions.act_window_close"}
