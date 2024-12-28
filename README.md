# Seminar Urban Computing 2024

This repository is used for the Seminar Urban Computing 2024 for the project "Housing Data made visible"

For running the project please see the corresponding documentation. 

For a complete Fullload of the data run the commands on linux in the following order:
Start the docker container with: 
```
docker compose up --build -d
```
Given, that the Docker container is up and running:

For the basic setup:
```
./setup_scripts/install_dependencies.sh
```

For then running the full import:
```
./run.sh
```