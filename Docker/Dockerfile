FROM python:3.8-slim

WORKDIR /var/www/apiservice/

COPY requirements.txt /var/www/apiservice/requirements.txt

COPY Bin/api.py /var/www/apiservice/api.py
COPY Bin/starter.sh /var/www/apiservice/starter.sh

COPY config.py /var/www/apiservice/config.py
COPY ./lib/ /var/www/apiservice/lib/ 
 

RUN pip install --no-cache-dir -r /var/www/apiservice/requirements.txt

ARG ENV
ENV ENV=${ENV}
ENV PYTHONPATH=.

EXPOSE 80
CMD ["uvicorn", "api:app", "--host=0.0.0.0", "--port=80", "--log-level=debug"]
