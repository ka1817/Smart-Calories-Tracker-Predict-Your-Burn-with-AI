FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 2001

CMD ["streamlit", "run", "app.py", "--server.port=2001", "--server.address=0.0.0.0"]

