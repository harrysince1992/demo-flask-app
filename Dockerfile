FROM python:3.12.5-slim
ARG FLASK_APP=app
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000
CMD ["python", "app.py" ]