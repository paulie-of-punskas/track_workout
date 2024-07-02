FROM python:3.9.19-alpine

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# install required packages
RUN pip install -r requirements.txt

COPY . /app

# add RW permissions for .csv file
RUN chmod 755 /app

# Expose the port that the application listens on.
EXPOSE 5000

# Register application
ENV FLASK_APP=track_workout

# Run Flask app
ENTRYPOINT ["gunicorn", "-c", "gunicorn_config.py", "track_workout:app"]
