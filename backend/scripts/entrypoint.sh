#!/bin/bash

echo "Applying migrations..."
python /app/backend/manage.py migrate
echo "All migrations applied!"

echo "Creating admin user..."
python /app/backend/manage.py initadmin

echo "Starting the server..."
python /app/backend/manage.py runserver 0.0.0.0:8000
