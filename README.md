# AEM Workspace

## Prerequisites

- Docker
    - [Linux](https://docs.docker.com/desktop/install/linux-install/)
    - [MacOS](https://docs.docker.com/desktop/install/mac-install/)
    - [Windows](https://docs.docker.com/desktop/install/windows-install/)
- Make sure "docker compose" is installed
    - [Docker Compose](https://docs.docker.com/compose/)

## Usage

Startup containers

```bash
docker compose up --build -d
```

Down containers

```bash
docker compose down
```

Excute only author container

```bash
docker compose run author --rm --service-ports -d 
```
