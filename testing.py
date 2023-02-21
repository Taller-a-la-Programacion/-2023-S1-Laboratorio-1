#NO MODIFICAR ESTE ARCHIVO

import Lab1;
import pytest;

    
def test_areaTrapecio_1():
    assert Lab1.areaTrapecio(10, 5, 5) == 37.5

def test_grupoPoblacion_1():
    assert Lab1.grupoPoblacion(15) == "Adolecentes"

def test_grupoPoblacion_2():
    assert Lab1.grupoPoblacion(5) == "Niños"
    
def test_grupoPoblacion_3():
    assert isinstance(str(Lab1.grupoPoblacion(-5)), str) == isinstance("Error: valor de edad desconocida", str)
    
    
def test_sonImpares_1():
    assert Lab1.sonImpares(1357) == True
    
def test_sonImpares_2():
    aassert Lab1.sonImpares(4131) == False
