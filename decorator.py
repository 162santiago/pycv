def Validate_Object(f):
    def wrapper(self, *args, **kwargs):
        data = f(self,*args, **kwargs)

        for key, value in data.items():
            if not value :
                raise ValueError(f"El Campo {key} esta vacio, asegurate de que los datos esten correctos")
        
        return data
    return wrapper

import mysql.connector
from mysql.connector import (errorcode)

def Validate_Conexion(f):
    def wrapper(self, connection_string,*args, **kwargs):
        try:
            data = f(self, connection_string,*args, **kwargs)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo está mal con tu nombre de usuario o contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database no existe")
            else:
                print(err)
        else:
            self._cnx.close()
        
    return wrapper
