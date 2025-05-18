# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app


#copy all files to the working directory
COPY . .

# Copy requirements file and install dependencies

RUN pip install --no-cache-dir -r requirements.txt


# Expose the Streamlit default port
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "app.py"]

