# Proyecto de Automatización de Pruebas Frontend

Este proyecto implementa un framework de automatización de pruebas para la aplicación web [Sauce Demo](https://www.saucedemo.com) utilizando Playwright con Python y siguiendo el patrón de diseño Page Object Model (POM).

## Estructura del Proyecto

```
Test-frontend-QA-Cod/
├── config.py                 # Configuración y constantes del proyecto
├── pages/                    # Implementación del patrón Page Object Model
│   ├── base_page.py          # Clase base para todas las páginas
│   ├── login_page.py         # Página de inicio de sesión
│   ├── product_page.py       # Página de productos
│   ├── cart_page.py          # Página del carrito
│   ├── checkout_page.py      # Página de checkout (paso 1)
│   ├── checkout_step_two_page.py  # Página de checkout (paso 2)
│   └── checkout_complete_page.py  # Página de confirmación de compra
├── tests/                    # Casos de prueba
│   └── test.py               # Implementación de los tests
└── utils/                    # Utilidades para las pruebas
    └── test_data_generator.py  # Generador de datos de prueba
```

## Requisitos

- Python 3.7+
- Playwright
- Pytest

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/dux14/Test-frontend-QA-Cod
cd Test-frontend-QA-Cod
```

2. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install pytest playwright pytest-html
playwright install chromium
```

## Configuración

El archivo `config.py` contiene todas las constantes y configuraciones necesarias para las pruebas:

- URLs de la aplicación
- Credenciales de usuario
- Datos de productos para pruebas
- Configuración para la generación de datos de prueba

## Casos de Prueba

El proyecto incluye los siguientes casos de prueba:

1. **test_login**: Verifica la funcionalidad de inicio de sesión.
2. **test_add_products_to_cart**: Verifica que se puedan agregar productos al carrito correctamente.
3. **test_verify_products_in_cart**: Verifica que los productos agregados aparezcan correctamente en el carrito.
4. **test_checkout_process**: Verifica el proceso completo de compra, desde el inicio de sesión hasta la confirmación.

## Ejecución de Pruebas

Para ejecutar todas las pruebas:

```bash
python -m pytest tests/test.py -v
```

Para generar un reporte HTML:

```bash
python -m pytest tests/test.py -v --html=report.html
```

## Generación de Datos de Prueba

El proyecto incluye un generador de datos de prueba que puede crear:

- Nombres aleatorios
- Apellidos aleatorios
- Códigos postales según el formato del país

La configuración para la generación de datos se encuentra en `config.py` en la sección `TEST_DATA_GENERATION`.

## Patrón Page Object Model

Este proyecto implementa el patrón Page Object Model (POM) para mejorar la mantenibilidad y reutilización del código:

- Cada página de la aplicación tiene su propia clase
- Las interacciones con la UI están encapsuladas en métodos específicos
- La lógica de prueba está separada de la implementación de la página

## Autor

Samuel Duque Porras
