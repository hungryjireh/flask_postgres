# Flask Postgres Container

## Application Overview

### Flask
The Flask backend connects to the Postgres database to store short links.  

To create new short links, you can make POST requests to /api/v1/create.

To access short links, you can make GET requests to /api/v1/<short_link>.

## Exploring the application

To verify whether the web application is running, you can visit the following links:

### Local: Dev Environment
- GET http://localhost:5000/api/v1/google
- POST http://localhost:5000/api/v1/create
```
{
    "url": "https://www.twitter.com",
    "url_reference": "twitter"
}

<!-- Visit http://localhost:3000/twitter thereafter -->
```
- GET http://localhost:3000/twitter
- GET http://localhost:3000

### Local: Production Environment
- GET http://localhost:1337/api/v1/google
- POST http://localhost:1337/api/v1/create
```
{
    "url": "https://www.twitter.com",
    "url_reference": "twitter"
}

<!-- Visit http://localhost:1337/twitter thereafter -->
```
- GET http://localhost:1337/twitter
- GET http://localhost:1337

## Running locally
After cloning this repository, run the following commands from the root folder:

```
<!-- Run from folder /flask_postgres -->
<!-- Create necessary configuration files -->
cp docker_app/frontend/app/.env.dev.example docker_app/frontend/app/.env.local
cp docker_app/.env.dev.example docker_app/.env.dev
cp docker_app/.env.dev.db.example docker_app/.env.dev.db

<!-- Spin up containers -->
cd docker_app
docker-compose up -d --build

<!-- Create SQL tables, seed DB with example entries -->
docker-compose exec web python manage.py create_db
docker-compose exec web python manage.py seed_db
```

## Deploying to the cloud
It is likely that you will have to install Git, Docker and Docker Compose beforehand.
You can follow these links to do so: [Installing Git](https://www.atlassian.com/git/tutorials/install-git) and [Installing Docker](https://docs.docker.com/engine/install/debian/)

After cloning this repository into a cloud environment, run the following commands from the root folder.
```
<!-- Run from folder /flask_postgres -->
<!-- Create necessary configuration files -->
<!-- In production, please ensure that you do not use the credentials provided for security reasons -->
cp docker_app/frontend/app/.env.prod.example docker_app/frontend/app/.env.local
cp docker_app/.env.prod.example docker_app/.env.prod
cp docker_app/.env.prod.db.example docker_app/.env.prod.db

<!-- Spin up containers -->
cd docker_app
docker-compose -f docker-compose.prod.yml up -d --build

<!-- Create SQL tables, seed DB with example entries -->
docker compose -f docker-compose.prod.yml exec web python manage.py create_db
docker compose -f docker-compose.prod.yml exec web python manage.py seed_db
```

## Stopping the application
```
<!-- Local: Dev Environment -->
docker-compose down

<!-- Local: Production Environment -->
docker-compose -f docker-compose.prod.yml down
```