# 1. Use an official lightweight Python runtime as a base image
FROM python:3.12-slim

# 2. Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy only the dependency list first to leverage Docker caching
COPY requirements.txt .

# 5. Install dependencies without saving local pip cache
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application source code
COPY . .

# 7. Expose the port your app runs on (change if using Flask, FastAPI, etc.)
EXPOSE 8000

# 8. Define the command to run your app
CMD ["python", "app.py"]
