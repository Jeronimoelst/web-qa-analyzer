from datetime import datetime

import pytest
from selenium.common.exceptions import WebDriverException

from analizador_web import setup, teardown
from generador_informes import guardar_informe


_RESULTADOS = {}


@pytest.fixture
def driver():
    navegador = setup()
    try:
        yield navegador
    finally:
        teardown(navegador)


def _registrar_resultado(item, estado, descripcion):
    navegador = item.funcargs.get("driver")
    url = None

    if navegador is not None:
        try:
            url = navegador.current_url
        except WebDriverException as error:
            descripcion = f"{descripcion} (No se pudo leer la URL: {error})"

    _RESULTADOS[item.nodeid] = {
        "test": item.nodeid,
        "fecha": datetime.now().isoformat(timespec="seconds"),
        "url": url,
        "resultado": estado,
        "descripcion": descripcion
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "setup":
        if report.passed:
            return
        estado = "SKIPPED" if report.skipped else "ERROR"
    elif report.when == "call":
        if report.passed:
            estado = "PASS"
        elif report.skipped:
            estado = "SKIPPED"
        elif call.excinfo is not None and isinstance(call.excinfo.value, AssertionError):
            estado = "FAIL"
        else:
            estado = "ERROR"
    elif report.when == "teardown":
        if not report.failed:
            return
        estado = "ERROR"
    else:
        return

    descripcion = "Test passed" if report.passed else str(report.longrepr)
    _registrar_resultado(item, estado, descripcion)


def pytest_sessionfinish(session, exitstatus):
    guardar_informe(list(_RESULTADOS.values()))
