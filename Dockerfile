FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHINUNBUFFERED 1
RUN mkdir /MANHWAyNL
WORKDIR /MANHWAyNL
COPY  requirements.txt /MANHWAyNL/
WORKDIR /MANHWAyNL
RUN pip install -r requirements.txt
COPY . /MANHWAyNL/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080

