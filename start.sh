#!/bin/bash

echo "Starting WasteBin Backend..."

cd server 

source .venv/bin/activate
uvicorn app:app --reload &

echo "Starting WasteBin Frontend..."

cd ../client
npm run dev

