"""Lop ket noi PostgreSQL, lay tu dap an bai lab buoi 6."""
import os
import time

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


def lay_ket_noi():
    if not DATABASE_URL:
        raise RuntimeError("Chua co DATABASE_URL trong moi truong.")
    return psycopg2.connect(DATABASE_URL)


def khoi_tao(so_lan: int = 15, cho_giay: int = 2):
    loi_cuoi = None
    for lan in range(1, so_lan + 1):
        try:
            conn = lay_ket_noi()
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS messages ("
                " id SERIAL PRIMARY KEY,"
                " role VARCHAR(20),"
                " content TEXT,"
                " created_at TIMESTAMP DEFAULT now())"
            )
            conn.commit()
            cur.close()
            conn.close()
            print(f"[db] Ket noi OK (lan thu {lan}).")
            return
        except Exception as e:  # noqa: BLE001
            loi_cuoi = e
            time.sleep(cho_giay)
    raise RuntimeError(f"Khong ket noi duoc CSDL sau {so_lan} lan: {loi_cuoi}")


def luu_tin_nhan(role: str, content: str) -> int:
    conn = lay_ket_noi()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO messages (role, content) VALUES (%s, %s) RETURNING id",
        (role, content),
    )
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return new_id


def doc_lich_su(gioi_han: int = 50):
    conn = lay_ket_noi()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        "SELECT id, role, content, created_at FROM messages"
        " ORDER BY created_at LIMIT %s",
        (gioi_han,),
    )
    ket_qua = cur.fetchall()
    cur.close()
    conn.close()
    return ket_qua
