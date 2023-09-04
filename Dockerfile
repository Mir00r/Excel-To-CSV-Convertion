# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install pandas
RUN pip install openpyxl

# Copy the script.py into the container
COPY converter.py /app/

# Run the Python script
CMD ["python", "converter.py"]
