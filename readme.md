# San pham cuoi khoa - ung dung chat nhieu container

## Kien truc

Ba service chay bang Docker Compose:

- `app`: ung dung FastAPI (main.py), cong 8000 trong mang noi bo.
- `db`: PostgreSQL 16, luu bang `messages`, du lieu nam o volume `pgdata`.
- `caddy`: reverse proxy, nhan cong 80 va 443, chuyen tiep sang `app:8000`,
  tu xin chung chi HTTPS.

## Cach chay bang Docker Compose

```bash
cp .env.example .env
docker compose up --build -d
docker compose logs -f app
```

Kiem tra: `curl http://localhost/health` tra ve `{"status":"ok"}`.

## Dia chi cong khai

https://vi-du.ptitai.org

## Kiem thu

```bash
pip install -r requirements.txt
pytest
```

Quy trinh CI o `.github/workflows/ci.yml` chay pytest va `docker build`
moi lan push hoac mo pull request.
