.EXPORT_ALL_VARIABLES:
COMPOSE_FILE ?= ./build/docker-compose/docker-compose.yml
IMAGE_CLASSIFIER_BACKEND ?= backend

.PHONY: help
help:
	@echo "\n\033[0;33mAvailable make commands:\033[0m\n"
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: start-server
start-server: build-backend build-frontend up  # Build all docker containers and start the server up

.PHONY: restart
restart: down up logs  # Restart running containers

.PHONY: up
up:  # Spin up the docker compose file
	docker compose -f $(COMPOSE_FILE) up -d
	docker compose ps

.PHONY: down
down:  # Stop all running containers
	docker compose down

.PHONY: logs
logs:  # Follow logs emitted by running containers
	docker compose logs --follow

.PHONY: connect
connect:  # Connect to the 'backend' container
	docker compose exec -it $(IMAGE_CLASSIFIER_BACKEND) /bin/bash

.PHONY: makemigrations
makemigrations:  # Create new migrations
	docker compose exec $(IMAGE_CLASSIFIER_BACKEND) python ./backend/manage.py makemigrations

.PHONY: migrate
migrate:  # Migrate unapplied migrations
	docker compose exec $(IMAGE_CLASSIFIER_BACKEND) python ./backend/manage.py migrate

.PHONY: build-backend
build-backend:  # Build Dockerfile for backend application
	docker build \
		--tag=image-classifier-backend \
		--file=build/docker/backend/Dockerfile-backend \
		backend/

.PHONY: build-frontend
build-frontend:  # Build Dockerfile for frontend application
	docker build \
		--tag=image-classifier-frontend \
		--file=build/docker/frontend/Dockerfile-frontend\
		frontend/
