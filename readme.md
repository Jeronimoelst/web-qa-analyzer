Fíjate en estos conceptos:
- webdriver.Chrome(): inicia el navegador Chrome.
- driver.get(): navega a una URL.
- driver.title: obtiene el título de la página.
- find_elements(): devuelve una lista de elementos que coinciden con el selector.
- driver.quit(): cierra el navegador y libera los recursos, incluso si ocurre un error dentro de try.
3. ¿Cómo integrar los tres temas?
Tema	Aplicación con Selenium
Web scraping	Extraer el título y los enlaces con driver.title y find_elements().
match/case	Clasificar los resultados de cada navegación.
break	Salir del bucle de entrada cuando el usuario escriba fin.


https://the-internet.herokuapp.com/?utm_source=chatgpt.com 
-pagina a testear
# Web QA Analyzer — Python & Selenium

## 1. Descripción del proyecto

Proyecto personal de **QA Automation** desarrollado con Python y Selenium WebDriver para automatizar comprobaciones sobre páginas web.

El objetivo es practicar la interacción con el navegador, la validación de elementos, el manejo de errores y la generación de informes de resultados.

El proyecto se desarrollará progresivamente, aplicando los conceptos aprendidos en Python a situaciones prácticas de testing.

## 2. Página web de pruebas

**The Internet — Herokuapp**

https://the-internet.herokuapp.com/

Esta web permite practicar diferentes escenarios de automatización, como formularios, checkboxes, alertas, tablas, ventanas emergentes, elementos dinámicos y carga de archivos.

## 3. Objetivos de aprendizaje

- Automatizar la navegación web con Selenium WebDriver.
- Localizar elementos mediante selectores.
- Obtener títulos, enlaces y textos de páginas web.
- Interactuar con botones, formularios y checkboxes.
- Utilizar esperas explícitas para gestionar elementos dinámicos.
- Aplicar `match/case` para clasificar resultados.
- Utilizar `while` y `break` para controlar la ejecución.
- Gestionar excepciones y registrar errores.
- Generar informes de ejecución.
- Aprender progresivamente a estructurar un proyecto de QA Automation.

## 4. Tecnologías

- Python 3.10 o superior.
- Selenium WebDriver.
- Google Chrome.
- Visual Studio Code.
- Git y GitHub para el control de versiones.

En fases posteriores se incorporarán `pytest` y herramientas de reporting.

## 5. Instalación

### Requisitos previos

Tener Python y Google Chrome instalados.

### Instalar Selenium

```bash
python -m pip install selenium
```

Selenium Manager puede gestionar automáticamente el controlador compatible con el navegador en las configuraciones habituales.

## 6. Estructura prevista

```text
web-qa-analyzer/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── analizador_web.py
│
├── tests/
│   └── test_navegacion.py
│
├── reports/
│   └── informe_web.txt
│
└── screenshots/
```

La estructura se ampliará conforme el proyecto incorpore nuevas funcionalidades.

## 7. Plan de desarrollo

### Fase 1 — Fundamentos de Selenium

- Inicializar WebDriver.
- Abrir una URL.
- Obtener el título y la URL actual.
- Localizar enlaces y contarlos.
- Cerrar el navegador correctamente.

### Fase 2 — Control de flujo en Python

- Solicitar URLs mediante un bucle `while`.
- Finalizar la entrada con `break`.
- Clasificar los resultados mediante `match/case`.
- Validar entradas vacías e incorrectas.

### Fase 3 — Interacción con la web

- Marcar y desmarcar checkboxes.
- Seleccionar opciones de listas desplegables.
- Rellenar formularios.
- Interactuar con alertas JavaScript.
- Trabajar con ventanas y pestañas.

### Fase 4 — Elementos dinámicos y robustez

- Implementar esperas explícitas.
- Gestionar excepciones de Selenium.
- Detectar elementos ausentes.
- Evitar esperas fijas innecesarias.
- Registrar los errores sin detener toda la ejecución.

### Fase 5 — Informes de QA

- Guardar resultados en un archivo.
- Contabilizar pruebas PASS, FAIL, ERROR y SKIPPED.
- Calcular porcentajes de éxito.
- Registrar fecha, URL y descripción del resultado.
- Revisar la información generada.

### Fase 6 — Evolución profesional

- Incorporar pytest.
- Separar las pruebas de la lógica auxiliar.
- Aplicar el patrón Page Object Model.
- Generar informes de pruebas automatizadas.
- Preparar el repositorio para presentarlo en un portfolio.

## 8. Criterios de calidad

- El navegador debe cerrarse correctamente incluso si ocurre un error.
- Las comprobaciones deben validar resultados esperados, no limitarse a imprimir información.
- Los errores deben registrarse de forma clara.
- Las esperas deben adaptarse al comportamiento de la página.
- El código debe ser legible, reutilizable y fácil de mantener.
- Cada nueva funcionalidad debe probarse antes de continuar.

**Importante:** el estado PASS o FAIL se determinará mediante condiciones verificables. Obtener un título o abrir una página no garantiza, por sí solo, que la prueba haya superado todas las validaciones.

## 9. Primer objetivo

Crear un programa que:

1. Abra la página principal de The Internet.
2. Compruebe que el título coincide con el esperado.
3. Obtenga la URL actual.
4. Cuente los enlaces disponibles.
5. Clasifique el resultado.
6. Permita repetir el proceso hasta introducir `fin`.
7. Guarde un informe con los resultados.

## 10. Estado del proyecto

- [ ] Preparar el entorno de Python.
- [ ] Instalar Selenium.
- [ ] Crear la estructura del proyecto.
- [ ] Automatizar la primera navegación.
- [ ] Integrar `match/case` y `break`.
- [ ] Implementar las primeras validaciones.
- [ ] Crear el informe de resultados.
- [ ] Añadir pruebas con pytest.
- [ ] Documentar el proyecto y publicarlo en GitHub.

---

**Autor:** Proyecto personal de aprendizaje de QA Automation.

**Lenguaje:** Python.

**Herramienta principal:** Selenium WebDriver. 