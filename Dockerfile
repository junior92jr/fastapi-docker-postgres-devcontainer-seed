# Specify the Python version for consistency
ARG VARIANT=3.11
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Set the user ID and group ID
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN if [ "$USER_GID" != "1000" ] || [ "$USER_UID" != "1000" ]; then \
    groupmod --gid $USER_GID vscode && usermod --uid $USER_UID --gid $USER_GID vscode; \
    fi

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    netcat-traditional gcc build-essential libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /workspace/requirements.txt
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r /workspace/requirements.txt

# Set up the workspace
WORKDIR /workspace
COPY . /workspace