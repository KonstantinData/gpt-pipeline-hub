# Dockerfile for GPT Pipeline Hub using Rye
FROM python:3.11-slim

# System dependencies
RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*

# Install Rye
ENV RYE_VERSION=latest
RUN curl -sSf https://rye.astral.sh/get | bash
ENV PATH="/root/.rye/shims:/root/.rye/bin:$PATH"

# Set workdir
WORKDIR /app

# Copy project files
COPY . /app

# Sync dependencies with Rye
RUN rye sync --no-lock

# Set entrypoint (can be overridden)
ENTRYPOINT ["rye", "run"]
CMD ["python", "cli/run_pipeline.py"]
