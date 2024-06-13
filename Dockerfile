
FROM python:3.10.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1


# Set work directory
WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
#RUN chmod x+ .wait-for-it.sh


COPY . .

EXPOSE 8000

CMD = ['python', 'manage.py', 'runserver', '0.0.0.0:8000'] 