import pytest

from analizador_urls import es_url_valida


@pytest.mark.parametrize(
    ("url", "esperada"),
    [
        ("https://example.com", True),
        ("http://example.com/ruta", True),
        ("https://sub.example.com/ruta?dato=1", True),
        ("example.com", False),
        ("ftp://example.com", False),
        ("https://", False),
        ("https://example", False),
        ("https://example..com", False),
        ("http://[::1", False),
        ("", False),
    ],
)
def test_es_url_valida(url, esperada):
    assert es_url_valida(url) is esperada
