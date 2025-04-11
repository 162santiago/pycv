import os
from pathlib import Path
class Files:

    def __init__(self):
        pass
    
    def generate_path(self, path):
        try:
            path_data = Path(__file__).parent / path
            path_data.mkdir(parents=True,exist_ok=True)
            return path_data
        except Exception as e:
            raise("Hubo un error al Crear la carpeta")
        
    def create_file(self,path, name_table):
        new_file = Path(path, f"{name_table}.csv")
        return new_file
