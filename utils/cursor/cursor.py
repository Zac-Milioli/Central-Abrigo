import sqlite3

class Cursor(sqlite3):
    def __init__(self, **args):
        super().__init__(**args)
        connection = sqlite3.connect(r'db/live_peixe.sql')
        self.cursor = connection.cursor()
