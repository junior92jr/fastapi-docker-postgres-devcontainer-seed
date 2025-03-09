# Specify the Python version for consistency
ARG VARIANT=3.11
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    DEBIAN_FRONTEND=noninteractive

# Set the user ID and group ID
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN if [ "$USER_GID" != "1000" ] || [ "$USER_UID" != "1000" ]; then \
    groupmod --gid $USER_GID vscode && usermod --uid $USER_UID --gid $USER_GID vscode; \
    fi

# Install necessary dependencies efficiently
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    netcat-traditional gcc build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel
RUN pip install --upgrade pip==24.0 setuptools==69.0.3 wheel==0.43.0

# Copy and install Python dependencies with proper ownership
COPY --chown=vscode:vscode requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r /workspace/requirements.txt

# Set up the workspace
WORKDIR /workspace
COPY --chown=vscode:vscode . /workspace
