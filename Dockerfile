# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /locationz

# Set the working directory to /locationz
WORKDIR /locationz

# Copy the current directory contents into the container at /music_service
ADD . /locationz/

COPY wait-for-it.sh /wait-for-it.sh
COPY start.sh /start.sh
RUN sed -i 's/\r//' /start.sh /wait-for-it.sh
RUN chmod +x /start.sh /wait-for-it.sh

# add dependencies
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update

#RUN apt install libpq-dev, gdal-bin
#RUN apt install -y binutils libpq-dev libproj-dev gdal-bin postgresql-client-11
RUN apt install -y  binutils \
    libproj-dev \
    gdal-bin

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt