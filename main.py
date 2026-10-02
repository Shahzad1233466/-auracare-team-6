# AuraCare Health System Core
APP_VERSION = "1.0.0"
MODULES_ENABLED = []

def patient_triage(symptoms):
    if symptoms == "severe":
        return "Emergency"
    elif symptoms == "moderate":
        return "Urgent"
    else:
        return "Normal"

def doctor_schedule(doctor):
    if doctor == "Dr. Ahmed":
        return "Monday to Friday"
    elif doctor == "Dr. Ali":
        return "Saturday and Sunday"
    else:
        return "Schedule not found"
