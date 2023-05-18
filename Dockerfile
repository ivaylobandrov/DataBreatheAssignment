FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY init-db.sh /init-db.sh

RUN chmod +x /init-db.sh

EXPOSE 8000

CMD ["/init-db.sh"]

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

CMD ["python", "-m", "pytest"]