FROM python:3.11

ARG WD=/opt/app
ARG GROUP=web
ARG USER=django

WORKDIR $WD

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

RUN groupadd -r $GROUP \
    && useradd -d $WD -r -g $GROUP $USER \
    && chown $USER:$GROUP -R $WD \
    && chown $USER:$GROUP /var/log

COPY --chown=$USER:$GROUP requirements.txt requirements.txt

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN apt-get update \
    && apt-get -y install gettext \
    && apt-get -y install netcat-traditional

COPY --chown=$USER:$GROUP bitrix24_integration ./bitrix24_integration
COPY --chown=$USER:$GROUP user_profiles ./user_profiles
COPY --chown=$USER:$GROUP templates ./templates
COPY --chown=$USER:$GROUP config ./config
COPY --chown=$USER:$GROUP entrypoint.sh ./entrypoint.sh
COPY --chown=$USER:$GROUP manage.py ./manage.py
COPY --chown=$USER:$GROUP uwsgi.ini ./uwsgi.ini

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh", "postgres", "5432"]