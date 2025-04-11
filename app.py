from database import Database

class App():
    def __init__(self):
        db = Database()
        db.extract_data_to_cv()

if __name__ == '__main__':
    App()