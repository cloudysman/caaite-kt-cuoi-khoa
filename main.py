"""Ung dung chat FastAPI - san pham cuoi khoa.

Ghep tu bai lab buoi 4 (CSDL), buoi 6 (nhieu container) va buoi 7 (kiem thu).
"""
from fastapi import FastAPI
from pydantic import BaseModel

import db
import llm

app = FastAPI(title="Chat app - san pham cuoi khoa")


@app.on_event("startup")
def startup():
    # Bo qua loi de ung dung van len duoc khi chay kiem thu ma khong co CSDL.
    try:
        db.khoi_tao()
    except Exception as e:  # noqa: BLE001
        print(f"[app] Chua ket noi duoc CSDL: {e}")


@app.get("/health")
def health():
    return {"status": "ok"}


class ChatIn(BaseModel):
    message: str


@app.post("/chat")
def chat(body: ChatIn):
    cau_hoi = body.message
    cau_tra_loi = llm.goi_llm(cau_hoi)
    db.luu_tin_nhan("user", cau_hoi)
    db.luu_tin_nhan("assistant", cau_tra_loi)
    return {"answer": cau_tra_loi}


@app.get("/history")
def history():
    return {"messages": db.doc_lich_su()}
