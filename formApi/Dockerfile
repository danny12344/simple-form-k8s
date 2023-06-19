FROM python:3.7.3-stretch

COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

RUN  pip install --upgrade pip && pip install -r /app/requirements.txt

EXPOSE 8000

#not sure if this is production ready
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]