FROM python:3.11-slim-bookworm

# Set working directory to the app folder where all your Python files are
WORKDIR /cs50_final/app

# Install Python dependencies
COPY requirements.txt ../
RUN pip install --no-cache-dir -r ../requirements.txt

# Copy the entire project
COPY . ..

# Run gunicorn from the app directory where app.py is located
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers=1", "--timeout=120", "app:app"]