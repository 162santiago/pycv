from pycvs.database import Database


class App():
    def __init__(self, app_name, version):
        self.get_info(app_name,version)
        db = Database()
        db.extract_data_to_cv()

    def get_info(self, app_name, version):
        print(f"Bienvenido a {app_name} v{version}")