import sqlite3
from datetime import datetime
from pathlib import Path

# Keep the database file in the project directory
DB_NAME = Path(__file__).resolve().parent.parent / "water_tracker.db"


def create_tables():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS water_intake (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                intake_ml INTEGER,
                date TEXT
            )
        """)


def log_intake(user_id, intake_ml):
    create_tables()

    date_today = datetime.now().strftime("%Y-%m-%d")

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            INSERT INTO water_intake (user_id, intake_ml, date)
            VALUES (?, ?, ?)
            """,
            (user_id, intake_ml, date_today)
        )


def get_intake(user_id):
    create_tables()

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            """
            SELECT intake_ml, date
            FROM water_intake
            WHERE user_id = ?
            ORDER BY id DESC
            """,
            (user_id,)
        )
        return cursor.fetchall()


if __name__ == "__main__":
    create_tables()
    log_intake("ashutosh", 1500)
    print("Database created successfully")
    print(get_intake("ashutosh"))