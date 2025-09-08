FROM python:3.11-slim-bookworm

# Install Chrome and system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/googlechrome-linux-keyring.gpg \
    && sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrome-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver (latest stable)
RUN wget -O /tmp/chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chromedriver-linux64.zip" \
    && unzip /tmp/chromedriver.zip \
    && mv chromedriver-linux64/chromedriver /usr/local/bin/ \
    && rm -rf /tmp/chromedriver.zip chromedriver-linux64 \
    && chmod +x /usr/local/bin/chromedriver

# Set display port to avoid crash
ENV DISPLAY=:99

# Set working directory to the app folder where all your Python files are
WORKDIR /cs50_final/app

# Install Python dependencies
COPY requirements.txt ../
RUN pip install --no-cache-dir -r ../requirements.txt

# Copy the entire project
COPY . ..

# Run gunicorn from the app directory where app.py is located
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers=1", "--timeout=120", "app:app"]