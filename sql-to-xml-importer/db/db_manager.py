import sqlite3

class DBManager:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL,
                    category TEXT
                )
            ''')

    def insert_products(self, product):
        with self.conn:
             self.conn.execute('''
                INSERT INTO products (id, name, price, category)
                VALUES (?, ?, ?, ?)
            ''', (product.id, product.name, product.price, product.category))
             
    def close(self):
        self.conn.close()