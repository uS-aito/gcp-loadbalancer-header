FROM python:3.6.8-slim

WORKDIR /root

RUN pip install flask

COPY main.py ./
EXPOSE 8000

USER 1

CMD ["python", "main.py", "8000"]