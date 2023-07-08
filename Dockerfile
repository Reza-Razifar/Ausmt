FROM python:latest
WORKDIR /app
COPY sum.py /app
CMD ["python","sum.py"]