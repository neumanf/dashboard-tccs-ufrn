# start by pulling the python image
FROM python:3.9-buster

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# copy every content from the local file to the image
COPY . /app

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt


EXPOSE 8080
# run
CMD ["gunicorn", "--bind", ":8080", "--chdir", "app", "dashboard:server"]