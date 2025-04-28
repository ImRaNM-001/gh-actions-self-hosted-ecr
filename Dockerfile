# Use official Python image with a non-root user and minimal layers
FROM python:3.12-slim

# Set environment variables for security
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a non-root user
RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

# Install uv securely
RUN pip install --no-cache-dir uv && \
    rm -rf /root/.cache

# Copy only necessary files first for better caching
COPY pyproject.toml ./
COPY uv.lock ./

# Install dependencies with uv
RUN uv pip install --system --no-cache

# Copy the rest of the code
COPY . .

# Change to non-root user
USER appuser

# Use a non-root port if running a server (optional)
EXPOSE 8080

ENTRYPOINT [ "uv" ]

CMD ["run", "calculator.py"]