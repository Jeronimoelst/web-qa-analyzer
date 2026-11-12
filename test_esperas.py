'''

Tu objetivo es automatizar el siguiente proceso:
1. Inicializar el navegador con setup().
2. Acceder a la página.
3. Localizar el botón Start.
4. Pulsar el botón.
5. Implementar una espera explícita para detectar el texto que aparece después de la carga.
6. Capturar una posible TimeoutException.
7. Registrar el error utilizando logging.
8. Comprobar mediante assert que aparece el texto Hello World!.
9. Cerrar el navegador con teardown().
Nuevos conceptos que debes aplicar:
- WebDriverWait
- expected_conditions
- TimeoutException
- logging.exception()
- assert
- try / except / finally
'''