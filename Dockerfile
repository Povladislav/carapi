FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --dev --system --deploy
COPY . /code/

COPY ./entrypoint.sh /
ENTRYPOINT ["sh","/entrypoint.sh"]