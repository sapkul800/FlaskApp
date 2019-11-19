FROM python:3.7-alpine
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
CMD ["python","application.py"]