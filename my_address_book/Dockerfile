FROM python:3.11

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . .

RUN pip install pipenv
RUN pipenv install

EXPOSE 5000

CMD ["python", "main.py"]