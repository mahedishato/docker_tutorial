FROM python:3.10.13

COPY . /mahedi
WORKDIR /mahedi

RUN pip install -r requirements.txt

ENV FLASK_APP app.py

EXPOSE 8087

CMD [ "flask", "run","--host=0.0.0.0", "--port=8087"]