import os

DEBUG=True
SECRET_KEY="THIS IS SECRET"

# DB CONFIG
DB_NAME=os.getenv("DV_NAME") or "trends"
DB_USER=os.getenv("DB_UNAME") or "root"
DB_PASSWORD=os.getenv("DB_PASS") or ""
DB_HOST=os.getenv("DB_HOST") or "localhost"