# e_commerce_py

## Descripción
Este proyecto es una aplicación de comercio electrónico desarrollada en Python. Utiliza una arquitectura modular con carpetas separadas para modelos, rutas, utilidades y configuración.

## Requisitos
Asegúrate de tener instalado lo siguiente:
- Python 3.10 o superior
- pip (gestor de paquetes de Python)

## Instalación
1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Instala un entorno virtual ejecutando:
   ```bash
   python -m venv venv
   ```
4. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto
```
README.md
requirements.txt
src/
    app.py
    config.py
    database/
        db.py
    models/
        MovieModel.py
        entities/
            Movie.py
    routes/
        Movie.py
    utils/
        DateFormat.py
```

## Uso
1. Activa el entorno virtual:
   ```bash
   source venv/Scripts/activate
   ```
2. Corre el proyecto:
   ```bash
   python src/app.py
   ```

## Notas
- Asegúrate de configurar correctamente el archivo `config.py` con los parámetros necesarios para la base de datos y otras configuraciones.
- El proyecto incluye un modelo de ejemplo (`MovieModel.py`) y rutas relacionadas (`routes/Movie.py`).

## Contribuciones
Si deseas contribuir a este proyecto, por favor sigue los pasos a continuación:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad o corrección de errores.
3. Realiza tus cambios y haz un commit con un mensaje claro.
4. Envía un pull request para revisión.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.