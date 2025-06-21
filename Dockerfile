FROM python:3.11

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# Install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port to avoid crash
ENV DISPLAY=:99

# Set working directory to the app folder where all your Python files are
WORKDIR /app/app

# Install Python dependencies
COPY requirements.txt ../
RUN pip install -r ../requirements.txt

# Copy the entire project
COPY . ..

# Now run gunicorn from the app directory where scrape.py is located
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers=1", "--timeout=300", "--worker-class=sync", "--max-requests=1", "--max-requests-jitter=1", "app:app"]