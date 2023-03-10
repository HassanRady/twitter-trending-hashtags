# pull official base image
FROM python:3.9-slim


# set work directory
WORKDIR /trending-hashtags


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# EXPOSE 9000

COPY . /trending-hashtags


# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]
