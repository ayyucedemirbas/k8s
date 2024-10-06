# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir tensorflow

# Run the inference script by default
CMD ["python", "inference.py"]
