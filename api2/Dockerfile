FROM python:3.10-slim
WORKDIR /app
COPY api2.py .
RUN pip install "fastapi[standard]"
CMD ["fastapi", "dev", "api2.py", "--host", "0.0.0.0", "--port", "8002"]
