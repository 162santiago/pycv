import os
import pandas as pd
from pycvs.file import Files
from dotenv import load_dotenv
from mysql.connector import (connection)
from pycvs.decorators.decorator import Validate_Object,Validate_Conexion, Transform_to_list

class Database:
    _cnx = None
    _file_manager = None
    _path = None

    def __init__(self):
        self._cnx = None
        self._file_manager = Files()        

        try:
            load_dotenv()
            self.get_conexion(self.define_config())

        except Exception as e:
            print(f"se encontro un error en el sistema, el error es:{e}")

    @Validate_Object
    def define_config(self):

        def search_data_env(value):
            return os.getenv(value)
        
        self._path = search_data_env('PATH_EXPORT_CVS')

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
            else:
                print("No se pudo establecer la conexión.")

    @Transform_to_list
    def search_tables_db(self):
        try:
            df = pd.read_sql_query("SHOW TABLES", self._cnx)
            return df.values.tolist()
        except Exception as e:
            raise ('error')
    
    def extract_data_to_cv(self):
        self._path= self._file_manager.generate_path(self._path)

        try:
            tables = self.search_tables_db()

            for table in tables:
                df = pd.read_sql_query(f"select * from {table}", self._cnx)
                archivo = self._file_manager.create_file(self._path, table)
                df.to_csv(archivo, quotechar='"',sep='|', index=False)

                # Verificar si el archivo fue guardado correctamente
                if os.path.exists(archivo):
                    print(f"El archivo '{archivo}' fue guardado correctamente.")
                else:
                    print("No se pudo guardar el archivo.")

            self.close_conexion()
            
        except Exception as e:
            print(e)
            pass
    
    def close_conexion(self):
        if self._cnx and self._cnx.is_connected():
            self._cnx.close()
            print("Conexión cerrada.")
        else:
            print("No hay conexión abierta para cerrar.")
           
