# this is an official Python runtime, used as the parent image
FROM python:3.9-slim

# Set environment variables
ENV SPOTIFY_CLIENT_ID=
ENV SPOTIFY_CLIENT_SECRET=
ENV SPOTIFY_REDIRECT_URI=http://localhost:8080

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    ffmpeg \
    libavcodec-extra \
    libavformat-dev \
    libavutil-dev \
    libswscale-dev \
    && rm -rf /var/lib/apt/lists/*

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 80 for the Flask app to run on
EXPOSE 80

# execute the Flask app
CMD ["python", "src/app.py"]
