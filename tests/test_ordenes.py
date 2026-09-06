from src.ordenes import estado_valido, transicion_valida, validar_datos_orden


def test_cp01_rechaza_falla_vacia():
    """CP-01: la falla reportada debe ser obligatoria."""
    errores = validar_datos_orden(
        cliente="Ana Pérez",
        dispositivo="Samsung A54",
        falla_reportada="",
    )

    assert "La falla reportada es obligatoria." in errores


def test_cp02_reconoce_estado_valido():
    """Comprueba que Recibido sea un estado permitido."""
    assert estado_valido("Recibido") is True


def test_cp03_rechaza_salto_directo_a_entregado():
    """CP-03: no se debe pasar directamente de Recibido a Entregado."""
    resultado = transicion_valida(
        estado_actual="Recibido",
        estado_nuevo="Entregado",
    )

    assert resultado is False


def test_permita_pasar_de_recibido_a_diagnostico():
    """Comprueba una transición válida del proceso técnico."""
    resultado = transicion_valida(
        estado_actual="Recibido",
        estado_nuevo="En diagnóstico",
    )

    assert resultado is True
