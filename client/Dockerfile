FROM python:3.9.6

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
