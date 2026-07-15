import sqlite3
from datetime import datetime


class MemoryStore:
    def __init__(self, path="jarvis_memory.db"):
        self.connection = sqlite3.connect(path)
        self.create_table()

    def create_table(self):
        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY,
            content TEXT,
            created_at TEXT
        )
        """)
        self.connection.commit()

    def save(self, content):
        self.connection.execute(
            """
            INSERT INTO memories
            (content, created_at)
            VALUES (?,?)
            """,
            (
                content,
                datetime.utcnow().isoformat()
            )
        )
        self.connection.commit()

    def get_all(self):
        result = self.connection.execute(
            "SELECT content FROM memories"
        )
        return [
            row[0]
            for row in result.fetchall()
        ]