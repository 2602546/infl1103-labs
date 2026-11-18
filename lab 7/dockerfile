FROM python:3.11-slim

WORKDIR /app

COPY auditor.py .
COPY modular_auditor.py .
COPY persistent_auditor.py .
COPY inventory_manager.py .

CMD ["python", "inventory_manager.py"]