# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy everything into the container
COPY . .

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt

# Run the program by default (pass "large", "small" or other directory if needed)
CMD ["python", "week1-search/projects/project1/degrees.py"]
