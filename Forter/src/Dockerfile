LABEL authors="Chen Frydman"

# Base image with Python 3.9
FROM python:3.9

# Set working directory
WORKDIR /app

# Install dependencies (assuming nicknames is a custom library) \
# Copy nicknames directory if it's local
COPY nicknames .
RUN pip install -r requirements.txt  # Install dependencies from requirements.txt (if applicable)

# Copy all files from current directory
COPY . .

  # Execute the Python script
CMD ["python", "name_count.py"]