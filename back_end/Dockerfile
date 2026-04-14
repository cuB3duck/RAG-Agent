# Use the latest version of Python
FROM python:3.12-slim
 
# Set the working directory inside the container
WORKDIR /app
 
# Copy Python dependencies
COPY requirements.txt .
 
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application files
COPY . .
 
# Expose the port your app runs on
EXPOSE 5000
 
# Define the command to run your app
CMD ["python", "Main.py"]