# database.py
# File nay quan ly ket noi va truy van co so du lieu

import sqlite3
from config import Config

class DatabaseManager:
    def __init__(self):
        # Duong dan database lay tu config
        self.db_path = Config.DB_PATH
        self.connection = None

    def connect(self):
        """Ket noi den co so du lieu"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            print("Ket noi den database thanh cong")
        except sqlite3.Error as e:
            print(f"Loi ket noi database: {e}")

    def disconnect(self):
        """Ngat ket noi den co so du lieu"""
        if self.connection:
            self.connection.close()
            print("Da ngat ket noi database")

    def execute_query(self, query, params=()):
        """Thuc thi mot cau truy van"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Loi thuc thi truy van: {e}")
            return None

    def create_table(self):
        """Tao bang du lieu neu chua ton tai"""
        query = """
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            side TEXT NOT NULL,
            price REAL NOT NULL,
            quantity REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
        """
        self.execute_query(query)

# Khoi tao instance
db_manager = DatabaseManager()