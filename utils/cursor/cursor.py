import sqlite3

class Cursor:
    def __init__(self):
        connection = sqlite3.connect(r'db/live_peixe.sql')
        self.cursor = connection.cursor()

    def create_abrigo(self):
        pass

    def get_abrigo(self):
        pass

    def update_abrigo(self):
        pass

    def delete_abrigo(self):
        pass

    def create_mantimento(self):
        pass

    def get_mantimento(self):
        pass
    
    def update_mantimento(self):
        pass

    def delete_mantimento(self):
        pass

    