#!/bin/bash
echo "Running migrations"
alembic upgrade head
echo "Running server"
uvicorn main:app --host 0.0.0.0 --port 8080
