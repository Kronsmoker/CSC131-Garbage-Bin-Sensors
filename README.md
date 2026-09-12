Smart-Waste-Bin project fro monitoring water-bin fill levels.
# CSC131 Garbage Bin Sensors

Initial prototype for a smart campus waste-bin monitoring system.

## Current Features

* React frontend
* FastAPI backend
* PostgreSQL database
* Fake sensor endpoint that creates and saves test readings

## Before You Start

You need these installed:

* Git
* Node.js
* Python 3
* PostgreSQL

## First-Time Setup

Clone the project:

```bash
git clone https://github.com/Kronsmoker/CSC131-Garbage-Bin-Sensors.git
cd CSC131-Garbage-Bin-Sensors
```

Install frontend packages:

```bash
cd client
npm install
cd ../server
```

Create the Python virtual environment and install backend packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi "uvicorn[standard]" sqlalchemy psycopg2-binary
```

Create the local PostgreSQL database:

```bash
createdb wastebin
cd ..
```

## Run the App

From the main project folder:

```bash
./start.sh
```

Open the frontend:

```text
http://localhost:5173
```

## Test the Fake Sensor

With the app running, open:

```text
http://127.0.0.1:8000/sensors/fake-reading
```

This creates a fake sensor reading and saves it to the local PostgreSQL database.

