from suma import sumar

def test_suma_valida():
    resultado = sumar(8, 7)
    assert 0 <= resultado <= 20, f"Resultado {resultado} fuera del rango válido [0-20]"
