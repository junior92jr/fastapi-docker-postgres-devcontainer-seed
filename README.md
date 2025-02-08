# fastapi-docker-postgres-devcontainer-seed  

**Description**:  
A pre-configured FastAPI project seed designed to streamline development with Docker, PostgreSQL, and Visual Studio Code DevContainers. This template is perfect for developers looking to kickstart a scalable FastAPI app with a PostgreSQL database, all within a containerized, reproducible environment.  

## Features:  
- **FastAPI** as the primary backend framework for building high-performance APIs.  
- **PostgreSQL** database integration for robust data management.  
- **Docker Compose** configuration for quick setup and isolated development.  
- **DevContainers** support for seamless VS Code integration, allowing easy onboarding and consistent environments.  
- **Supports non-VS Code users** via standard Docker Compose setup.  

## Getting Started  

### For VS Code Users:  
1. Clone the repository and open it in VS Code.  
2. Open the DevContainer (`.devcontainer/devcontainer.json`) to automatically set up the development environment.  
3. Run the application using Docker Compose to start the FastAPI app with a connected PostgreSQL database.  

### For Non-VS Code Users:

If you are not using Visual Studio Code but still want to use the seed project, follow these steps:

1. Ensure you have **Docker** and **Docker Compose** installed on your system.
2. Clone the repository:

#### HTTPS

Use the following command to clone via HTTPS:
```bash
git clone https://github.com/junior92jr/fastapi-docker-postgres-devcontainer-seed.git
cd fastapi-docker-postgres-devcontainer-seed
```

#### SSH

Alternatively, you can clone via SSH (make sure your SSH keys are set up):
```bash
git clone git@github.com:junior92jr/fastapi-docker-postgres-devcontainer-seed.git
cd fastapi-docker-postgres-devcontainer-seed
```

3. Set up the `.env` file:

Copy the example `.env_sample` file to create your own `.env` file:
```bash
cp .env_example .env
```

4. (Optional) Edit the `.env` file:

Open the `.env` file and update any environment variables as needed, such as database configurations or API keys.


5. Build and start the Docker containers:

There are two possible commands depending on your Docker version:

##### For older versions of Docker (with `docker-compose`):
```bash
docker-compose up --build
```
This command tells Docker Compose to:

Build the images if they aren't already built.
Start the containers based on the configurations in the `docker-compose.yml` file.

##### For newer versions of Docker (with `docker compose`):
```bash
docker compose up --build
```

In the newer Docker versions, the command is slightly different (notice the space between `docker` and `compose`). It functions the same way as the previous command.


6. Access the application:

Once the containers are running, you can access the FastAPI app by navigating to `http://localhost:<port>` (replace `<port>` with the port configured in your `.env` or `docker-compose.yml` file).


7. (Optional) Run in detached mode:

If you want to run the containers in the background, use the `-d` flag:

```bash
docker-compose up --build -d
```

or, for newer versions:

```bash
docker compose up --build -d
```
This will run the containers in detached mode, freeing up your terminal.

8. Stop the containers:
When you're done, you can stop the containers with:
```bash
docker-compose down
```

or, for newer versions:

```bash
docker compose down
```


### Running Tests with pytest:
Once your Docker containers are up and running, you can run tests using pytest within the container.

Access the running container (e.g., the app container) using Docker's `exec` command:
```bash
docker exec -it <container_name> /bin/bash
```

Replace `<container_name>` with the name of your app container, which you can find by running:

```bash
docker ps
```

Once inside the container, navigate to the project directory (if not already there):

```bash
cd /path/to/your/project
```

Run pytest to execute your tests:

```bash
pytest
```

This will run all the tests located in the project. If you have specific test directories or files, you can also specify them, like so:

```bash
pytest path/to/test_file.py
```

After running the tests, you can exit the container:

```bash
exit
```
