import os
from mysql.connector import (connection)
from dotenv import load_dotenv
from decorator import Validate_Object,Validate_Conexion
import pandas as pd

class Database:
    def __init__(self):
        self._cnx = None

        try:
            load_dotenv()
            self.get_conexion(self.define_config())

        except Exception as e:
            print(f"se encontro un error en el sistema, el error es:{e}")

    @Validate_Object
    def define_config(self):

        def search_data_env(value):
            return os.getenv(value)
        
        env_data = {
            'host' : search_data_env('DB_HOST'),
            'user' : search_data_env('DB_USER'),
            'password' : search_data_env('DB_PASSWORD'),
            'database' : search_data_env('DB_NAME')
        }

        #sobreescribe el atributo de la clase 
        # for  key, value in env_data.items():
        #     setattr(self, key, value)
        return env_data
    
    @Validate_Conexion
    def get_conexion(self, connection_string):
            self._cnx = connection.MySQLConnection(**connection_string)
            if self._cnx and self._cnx.is_connected():
                print("Conexión exitosa")
                self.query()
            else:
                print("No se pudo establecer la conexión.")

    def query(self,):
        df = pd.read_sql_query("SHOW TABLES", self._cnx)
        print(df)
        self.cerrar_conexion()
    
    def cerrar_conexion(self):
        if self._cnx and self._cnx.is_connected():
            self._cnx.close()
            print("Conexión cerrada.")
        else:
            print("No hay conexión abierta para cerrar.")
           
db = Database()
