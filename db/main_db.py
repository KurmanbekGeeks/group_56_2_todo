import sqlite3
from db import queries
from config import db_path


def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TASKS)
    cursor.execute(queries.TEST_CREATE)
    print('База данных подключена!')
    conn.commit()
    conn.close()