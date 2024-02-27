
from test_cardapio import calcular_total_pedido

def test_pedido_valido():
    codigos_pedido = [100, 101, 200, 201]
    assert calcular_total_pedido(codigos_pedido) == 29.0

def test_pedido_com_codigo_invalido():
    codigos_pedido = [100, 105, 300]
    assert calcular_total_pedido(codigos_pedido) == 26.0  # Somente códigos válidos devem ser considerados

def test_pedido_vazio():
    codigos_pedido = []
    assert calcular_total_pedido(codigos_pedido) == 0.0

def test_pedido_com_produtos_repetidos():
    codigos_pedido = [100, 100, 101, 101, 200, 200]
    assert calcular_total_pedido(codigos_pedido) == 58.0  # Cada produto deve ser contado apenas uma vez
