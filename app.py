import os
import psycopg
from flask import Flask

app = Flask(__name__)
DB = os.getenv("DATABASE_URL")


@app.get("/")
def home():
    return {"message": "Hello from Docker!"}


@app.get("/visits")
def visits():
    with psycopg.connect(DB) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY, at TIMESTAMP DEFAULT now())")
        conn.execute("INSERT INTO visits DEFAULT VALUES")
        count = conn.execute("SELECT count(*) FROM visits").fetchone()[0]
    return {"visits": count}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)