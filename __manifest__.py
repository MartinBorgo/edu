{
    "name": "Educatión",
    "summery": "An education platform to track students",
    "author": "Martin Borgo",
    "category": "Uncategorized",
    "application": True,
    "version": "19.0.1.0.0",
    "depends": ["base"],
    "data": [
        # Security
        "security/security.xml",
        "security/ir.model.access.csv",
        # Wizards
        "wizards/edu_attendance_wizard.xml",
        # Views
        "views/edu_season_view.xml",
        "views/edu_student_view.xml",
        "views/edu_course_view.xml",
        "views/edu_course_instance_view.xml",
        "views/menu.xml",
    ],
    "license": "LGPL-3",
}
