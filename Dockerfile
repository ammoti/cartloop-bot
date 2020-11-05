# base image
FROM python:3

#maintainer
LABEL Author="Vahap"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app/
COPY requirements.txt /app/
EXPOSE 8000
RUN pip install -r requirements.txt



# RUN python manage.py makemigrations --noinput
# RUN python manage.py migrate --noinput
# RUN python manage.py loaddata data

CMD python manage.py runserver 0.0.0.0:8000
