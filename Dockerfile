FROM python:3.11-alpine

ENV APP_HOME=/app \
    POETRY_VERSION=1.6.1

WORKDIR $APP_HOME

VOLUME [ "${APP_HOME}/ex_4/storage/" ]

COPY . .

RUN pip install "poetry==$POETRY_VERSION"

RUN poetry install --no-root

EXPOSE 3000

ENTRYPOINT [ "poetry", "run", "start-server" ]