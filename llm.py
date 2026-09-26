"""LLM gia lap, giu nguyen tu cac bai lab truoc."""


def goi_llm(cau_hoi: str) -> str:
    cau_hoi = (cau_hoi or "").strip()
    if not cau_hoi:
        return "(LLM gia lap) Ban chua nhap gi ca."
    return f"(LLM gia lap) Minh da nhan duoc cau hoi: {cau_hoi}"
