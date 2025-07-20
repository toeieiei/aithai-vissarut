FROM python:3.10-slim
WORKDIR /app
COPY api1.py .
RUN pip install "fastapi[standard]" requests
CMD ["fastapi", "dev", "api1.py", "--host", "0.0.0.0", "--port", "8001"]
