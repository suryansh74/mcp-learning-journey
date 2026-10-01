FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir "mcp[cli]>=2.0.0"

COPY server.py .

EXPOSE 8000

CMD ["python", "server.py"]
