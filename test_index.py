import os

def test_html_existe():
    assert os.path.exists("index.html"), "El archivo index.html no existe"

def test_contenido_hola_mundo():
    with open("index.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    assert "Hola Mundo" in contenido, "El texto 'Hola Mundo' no se encontró en index.html"