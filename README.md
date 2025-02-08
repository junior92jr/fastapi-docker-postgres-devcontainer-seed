# FastAPI Docker PostgreSQL DevContainer Seed

**Description**A pre-configured FastAPI project template designed to streamline development with Docker, PostgreSQL, and Visual Studio Code DevContainers. This template is perfect for developers who want to quickly get started with a scalable FastAPI application using a PostgreSQL database, all within a containerized, reproducible environment.

---

## 🚀 Features

- **FastAPI**: High-performance framework for building APIs with Python 3.7+.
- **PostgreSQL**: Robust, open-source relational database for data management.
- **Docker Compose**: Simplified multi-container management for easy setup and isolated development environments.
- **DevContainers**: Seamless integration with Visual Studio Code, offering a consistent and reproducible development environment.
- **Standard Docker Setup**: Supports non-VS Code users with a straightforward Docker Compose configuration.

---

## 💡 Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- **Docker** & **Docker Compose** (for containerization)
- **Visual Studio Code** (optional, for DevContainer integration)
- **Git** (to clone the repository)

---

### 🖥️ For Visual Studio Code Users

1. **Clone the repository**:

   ```bash
   git clone https://github.com/junior92jr/fastapi-docker-postgres-devcontainer-seed.git
   cd fastapi-docker-postgres-devcontainer-seed
   ```

2. **Open the project in VS Code**:   Open the project folder in Visual Studio Code.

3. **Automatically configure your DevContainer**:   Once inside VS Code, it will automatically prompt you to reopen the folder inside the DevContainer (defined in `.devcontainer/devcontainer.json`).

4. **Run the application**:   Use Docker Compose to start the FastAPI app along with the PostgreSQL database by running:

   ```bash
   docker-compose up --build
   ```

   The application will be running and available at `http://localhost:<port>` (where `<port>` is defined in your `.env` file).

---

### 🛠️ For Non-VS Code Users

1. **Clone the repository**:

   ```bash
   git clone https://github.com/junior92jr/fastapi-docker-postgres-devcontainer-seed.git
   cd fastapi-docker-postgres-devcontainer-seed
   ```

2. **Set up the `.env` file**:   Copy the example `.env_sample` file to create your own `.env` file.

   ```bash
   cp .env_sample .env
   ```

3. **Edit the `.env` file (Optional)**:   Open and edit the `.env` file to update any environment variables (e.g., database configurations, API keys).

4. **Build and start the Docker containers**:

   For **older Docker versions** (using `docker-compose`):

   ```bash
   docker-compose up --build
   ```

   For **newer Docker versions** (using `docker compose`):

   ```bash
   docker compose up --build
   ```

   This will build the necessary images and start the containers, creating the FastAPI app connected to a PostgreSQL database.

5. **Access the application**:   Once the containers are running, open a browser and go to `http://localhost:<port>` (replace `<port>` with the port configured in `.env` or `docker-compose.yml`).

6. **Run in detached mode (Optional)**:   To run the containers in the background, use the `-d` flag:

   For **older Docker versions**:

   ```bash
   docker-compose up --build -d
   ```

   For **newer Docker versions**:

   ```bash
   docker compose up --build -d
   ```

7. **Stop the containers**:   To stop the containers when you're done, use:

   For **older Docker versions**:

   ```bash
   docker-compose down
   ```

   For **newer Docker versions**:

   ```bash
   docker compose down
   ```

---

## 🧪 Running Tests

1. **Access the running container**:

   Use the following command to access the app container:

   ```bash
   docker exec -it <container_name> /bin/bash
   ```

   Replace `<container_name>` with the name of your app container, which you can find by running:

   ```bash
   docker ps
   ```

2. **Navigate to the project directory** (if not already there):

   ```bash
   cd /path/to/your/project
   ```

3. **Run the tests**:

   Execute the tests using `pytest`:

   ```bash
   pytest
   ```

   You can also specify specific test files or directories:

   ```bash
   pytest path/to/test_file.py
   ```

4. **Exit the container**:

   Once done, exit the container:

   ```bash
   exit
   ```

---

## 📝 Additional Notes

- If you're using **Docker Desktop**, you can easily manage containers through the GUI interface.
- This template uses **Docker Compose** to manage multi-container environments for both development and production.
- The `.env` file includes various environment variables for configuration—make sure to customize it according to your needs.
- To customize the FastAPI application, simply modify the code in the `app` directory.

---

## 🎯 Contributing

Feel free to fork this project and submit pull requests! Contributions are always welcome.
