import regex as re

def validate_propuesta_taller(form):
    def string_not_empty(field):
        if not field.strip():
            return False
        return True
    
    def string_length(field, max_length):
        if len(field) > max_length:
            return False
        return True
    
    def integer_range(field, min_value, max_value):
        if field < min_value or field > max_value:
            return False
        return True

    def email(field):
        return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+$", field)
    
    nombre = form.get("nombre")
    apellidos = form.get("apellidos")
    experiencia = form.get("experiencia")

    correo = form.get("correo")
    telefono = form.get("telefono")

    nombre_taller = form.get("nombre-taller")
    descripcion = form.get("descripcion")
    modalidad = form.get("modalidad")
    materiales = form.get("materiales")
    try:
        vacantes = form.get("vacantes")
        if vacantes:
            vacantes = int(vacantes)
        else:
            vacantes = 0
        sesiones = form.get("sesiones")
        if sesiones:
            sesiones = int(sesiones)
        else:
            sesiones = 0
    except ValueError:
        return False

    if not all([
        string_not_empty(nombre),
        string_not_empty(apellidos),
        string_not_empty(experiencia),
        string_length(experiencia, max_length=500),
        string_not_empty(correo),
        string_not_empty(telefono),
        string_not_empty(nombre_taller),
        string_not_empty(descripcion),
        string_length(descripcion, max_length=500),
        modalidad in ["presencial", "online"],
        string_length(materiales, max_length=500),
        integer_range(vacantes, min_value=0, max_value=100),
        integer_range(sesiones, min_value=0, max_value=20),
        email(correo)
    ]):
        return False
    return True
