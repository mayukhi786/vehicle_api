This project is a CRUD-style API service for managing vehicle data. It allows users to perform operations such as creating, retrieving, updating, and deleting vehicle records stored in an SQLite database. The service is implemented using **FastAPI** and **SQLAlchemy**.

## Features
- **Create Vehicle**: Add a new vehicle record with a unique VIN.
- **Retrieve All Vehicles**: Get a list of all stored vehicles.
- **Retrieve Vehicle by VIN**: Fetch a specific vehicle using its VIN.
- **Update Vehicle by VIN**: Modify an existing vehicle's details.
- **Delete Vehicle by VIN**: Remove a vehicle from the database.

## Requirements
- Python 3.9+
- pipenv or virtualenv (for environment management)
- SQLite (pre-installed with Python)

## Setup Instructions

### Clone the Repository
```bash
git clone <repository-url>
cd vehicle_api
```
## Create a Virtual Environment and Install Dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
pip install -r requirements.txt
```
## Run the Application
## Start the application using uvicorn:
```bash
uvicorn app.main:app --reload
```
Access the API at: http://127.0.0.1:8000

See endpoints with Swagger UI at: http://127.0.0.1:8000/docs/

## Run Tests
```bash
pytest
```
## API Endpoints
## 1. Create Vehicle

POST /vehicle

Request Body:

```json

{
  "vin": "1HGCM82633A123456",
  "manufacturer_name": "Honda",
  "description": "Reliable car",
  "horse_power": 180,
  "model_name": "Accord",
  "model_year": 2020,
  "purchase_price": 20000.00,
  "fuel_type": "Gasoline"
}
```

Response:

201 Created: Returns the created vehicle.
422 Unprocessable Entity: Validation or duplicate VIN error.

## 2. Retrieve All Vehicles

GET /vehicle

Response:

200 OK: Returns a list of all vehicles.

## Retrieve Vehicle by VIN
GET /vehicle/{vin}

Response:

200 OK: Returns the vehicle with the specified VIN.
404 Not Found: VIN does not exist.

## 4. Update Vehicle by VIN
PUT /vehicle/{vin}

Request Body:

```json
{
  "manufacturer_name": "Toyota",
  "description": "Updated description",
  "horse_power": 200,
  "model_name": "Camry",
  "model_year": 2021,
  "purchase_price": 22000.00,
  "fuel_type": "Hybrid"
}
```

Response:

200 OK: Returns the updated vehicle.
404 Not Found: VIN does not exist.


## 5. Delete Vehicle by VIN
DELETE /vehicle/{vin}

Response:

204 No Content: Vehicle successfully deleted.
404 Not Found: VIN does not exist.

Development and Testing
Database Management
Use SQLite for development. The database is automatically created with the required schema.

## To inspect the database:

```bash
sqlite3 vehicle_data.db
```
Fixtures for Testing
The project uses pytest for testing. Test fixtures are located in app/tests/conftest.py.

Run tests with:

```bash
pytest
```
