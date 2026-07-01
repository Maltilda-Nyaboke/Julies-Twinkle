#!/bin/bash

# Run migrations
echo "Running migrations..."
python3 manage.py migrate

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Build complete!"
