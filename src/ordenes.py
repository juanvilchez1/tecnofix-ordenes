ESTADOS_ORDEN = [
    "Recibido",
    "En diagnóstico",
    "En reparación",
    "Listo para retirar",
    "Entregado",
    "Cancelado",
]


def validar_datos_orden(cliente, dispositivo, falla_reportada):
    """Valida los campos obligatorios de una orden de reparación."""
    errores = []

    if not cliente or not cliente.strip():
        errores.append("El cliente es obligatorio.")

    if not dispositivo or not dispositivo.strip():
        errores.append("El dispositivo es obligatorio.")

    if not falla_reportada or not falla_reportada.strip():
        errores.append("La falla reportada es obligatoria.")

    return errores


def estado_valido(estado):
    """Comprueba si el estado pertenece a la lista permitida."""
    return estado in ESTADOS_ORDEN
