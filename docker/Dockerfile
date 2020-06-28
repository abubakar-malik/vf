FROM python:3.7.7-buster

ARG PORT
ARG DB_NAME
ARG DB_USERNAME
ARG DB_PASSWORD
ARG DB_CONNECTIONSTRING

ENV PORT=${PORT}
ENV DB_NAME=${DB_NAME}
ENV DB_USERNAME=${DB_USERNAME}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_CONNECTIONSTRING=${DB_CONNECTIONSTRING}

RUN apt-get update && \
    apt-get install -y  build-essential python-dev python-pip default-mysql-client default-libmysqlclient-dev && \
    pip install --upgrade flask flask-mysql markupsafe && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

# Creating and copy contents to /app in container
WORKDIR /app
ADD . /app

CMD ["python", "sample.py"]
EXPOSE ${PORT}
