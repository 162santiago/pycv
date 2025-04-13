<p align="center"><a href="https://www.python.org/downloads/" target="_blank"><img src="https://www.python.org/static/img/python-logo.png" width="400" alt="Laravel Logo"></a></p>

# Pycvs

## Descripción del Proyecto

Esta es una pequeña aplicación desarrollada en Python, diseñada para extraer datos desde una base de datos MySQL utilizando la biblioteca `mysql-connector-python`. El objetivo principal es convertir todas las tablas de la base de datos al formato CSV, de manera que puedan ser utilizadas fácilmente en herramientas como Power BI o Excel.


## Requisitos

- Python 3
- Pandas
- mysql-connector-python
- python-dotenv

## Instalación

1. Clona este repositorio en tu máquina local 

    ```bash
    https://github.com/162santiago/pycv.git
    ```

2. Navega hasta el directorio del proyecto:

    ```bash
    cd pycv
    ```

3. Crea un Entorno Virtual:

    ```bash
    python -m venv venv
    ```
4. Activa el Entorno Virtual:

    ```bash
    venv\Scripts\activate
    ```

5. Instala las dependencias de Python:

    ```bash
    pip install -r requirements.txt
    ```

6. Crea una copia del archivo `.env.example` y renómbrala a `.env`:

    ```bash
    cp .env.example .env
    ```
7. configura las variables de entorno en  `.env` :

    ```bash
    DB_HOST = "127.0.0.1"
    DB_USER = "example"
    DB_PASSWORD = "example"
    DB_NAME = "example"
    PATH_EXPORT_CVS = "data/"
    ```
8. Ejecuta el Paquete con:

    ```bash
    python -m pycvs  
    ```
