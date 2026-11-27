# Proyecto final QA Automation Testing

Framework de pruebas UI y API con Python, Pytest, Selenium, Requests, POM y pytest-html. Incluye 9 escenarios UI y 5 API independientes. Los datos se leen desde `data/test_data.json`.

## Requisitos e instalación (Windows)

Python 3.10 o superior, Google Chrome e Internet. Selenium Manager gestiona el controlador de Chrome.

```powershell
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Estructura
- `pages/`: clases Page Object y acciones reutilizables.
- `tests/ui/`: login, inventario, carrito y checkout.
- `tests/api/`: GET, POST, DELETE y recurso inexistente.
- `data/`: credenciales demo y datos externos JSON.
- `utils/`: lectura de datos.
- `conftest.py`: fixtures y captura automática de fallos.
- `pytest.ini`: configuración y marcadores.
- `reports/`: resultados y capturas.

## Ejecución
Desde la raíz del proyecto:

```powershell
.\venv\Scripts\python.exe -m pytest
.\venv\Scripts\python.exe -m pytest -m ui
.\venv\Scripts\python.exe -m pytest -m api
.\venv\Scripts\python.exe -m pytest --collect-only
```

## Reportes
Abrir `reports/report.html` en el navegador. Passed indica éxito, Failed una validación fallida, Error un problema de preparación o limpieza, Skipped una prueba omitida. El reporte muestra duración y detalles. Los fallos UI durante preparación o ejecución con navegador disponible incluyen captura embebida y archivo PNG en `reports/screenshots/`. Los fallos API no tienen navegador. Cada ejecución reemplaza el reporte HTML; las capturas conservan fecha y hora.

## Independencia
Cada test UI usa una sesión nueva de Chrome y prepara sus propios datos. Las pruebas API no dependen de otras peticiones. JSONPlaceholder simula escrituras sin persistirlas. Se usan esperas explícitas y timeout HTTP.

## Casos
UI: login válido, contraseña incorrecta, usuario bloqueado, agregar producto, eliminar producto, ordenar precios, compra completa, checkout vacío, logout. API: listar publicaciones, consultar una, crear, eliminar, consultar inexistente.

## Estado de verificación
Código preparado para ejecutar localmente. No se incluyen resultados de ejecución real; verificar los 14 escenarios con acceso a los sitios demo antes de entregar.
