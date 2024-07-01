FROM python:3.9.19-alpine

# python version
ARG PYTHON_VERSION=3.9.6

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# upgrade pip and setuptools
RUN pip install --no-cache --upgrade pip setuptools

# install required packages
RUN pip install -r requirements.txt

COPY . /app

# add RW permissions for .csv file
RUN chmod 755 /app

# Expose the port that the application listens on.
EXPOSE 5001

# Register application
ENV FLASK_APP=track_workout

# Run Flask app
CMD python -m flask run --host=0.0.0.0
