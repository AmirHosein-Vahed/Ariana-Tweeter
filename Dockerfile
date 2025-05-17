FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app


RUN apk update && apk add --no-cache \
    build-base

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN apt install gunicorn
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

EXPOSE 8000

# Command to run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "twitter.wsgi:application"]
