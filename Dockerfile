FROM python:3.6.8-slim

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
EXPOSE 8000

USER 1

CMD ["python", "main.py", "8000"]