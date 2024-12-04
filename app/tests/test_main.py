from fastapi.testclient import TestClient
from app.main import app
import time

client = TestClient(app)

def test_create_vehicle():
    response = client.post("/vehicle", json={
        "vin": "1234567890",
        "manufacturer_name": "Honda",
        "description": "Reliable car",
        "horse_power": 180,
        "model_name": "Accord",
        "model_year": 2020,
        "purchase_price": 20000.00,
        "fuel_type": "Gasoline"
    })
    assert response.status_code == 201
    assert response.json()["vin"] == "1234567890"

def test_get_all_vehicles():
    client.post("/vehicle", json={
        "vin": "2345678901",
        "manufacturer_name": "Honda",
        "description": "Reliable car",
        "horse_power": 180,
        "model_name": "Accord",
        "model_year": 2020,
        "purchase_price": 20000.00,
        "fuel_type": "Gasoline"
    })

    # Fetch all vehicles
    response = client.get("/vehicle")

    assert response.status_code == 200
    vehicles = response.json()
    assert len(vehicles) > 0  # Check that there is at least one vehicle
    assert "vin" in vehicles[0]  # Check that the vin field exists


def test_get_vehicle_by_vin():
    # First, create a vehicle so that we have data to fetch
    response = client.post("/vehicle", json={
        "vin": "3456789012",
        "manufacturer_name": "Honda",
        "description": "Reliable car",
        "horse_power": 180,
        "model_name": "Accord",
        "model_year": 2020,
        "purchase_price": 20000.00,
        "fuel_type": "Gasoline"
    })

    vin = response.json().get("vin")

    # Fetch the vehicle by vin
    response = client.get(f"/vehicle/{vin}")

    assert response.status_code == 200
    vehicle = response.json()
    assert vehicle["vin"] == vin  # Check that the VIN matches
    assert "manufacturer_name" in vehicle  # Check that the manufacturer name exists

def test_update_vehicle():
    # First, create a vehicle so that we have data to update
    response = client.post("/vehicle", json={
        "vin": "4567890123",
        "manufacturer_name": "Honda",
        "description": "Reliable car",
        "horse_power": 180,
        "model_name": "Accord",
        "model_year": 2020,
        "purchase_price": 20000.00,
        "fuel_type": "Gasoline"
    })

    vin = response.json().get("vin")

    # Update the vehicle details
    response = client.put(f"/vehicle/{vin}", json={
        "vin": vin,
        "manufacturer_name": "Honda",
        "description": "Updated description",
        "horse_power": 200,
        "model_name": "Accord",
        "model_year": 2021,
        "purchase_price": 25000.00,
        "fuel_type": "Electric"
    })

    assert response.status_code == 200
    vehicle = response.json()
    assert vehicle["description"] == "Updated description"  # Check if the description was updated
    assert vehicle["horse_power"] == 200  # Check if horse power was updated

def test_delete_vehicle():
    # First, create a vehicle so that we have data to delete
    response = client.post("/vehicle", json={
        "vin": "5678901234",
        "manufacturer_name": "Honda",
        "description": "Reliable car",
        "horse_power": 180,
        "model_name": "Accord",
        "model_year": 2020,
        "purchase_price": 20000.00,
        "fuel_type": "Gasoline"
    })

    vin = response.json().get("vin")

    # Delete the vehicle by vin
    response = client.delete(f"/vehicle/{vin}")

    assert response.status_code == 204  # No content status for successful deletion

    # Try to fetch the deleted vehicle, it should not exist
    response = client.get(f"/vehicle/{vin}")
    assert response.status_code == 404  # Not found since the vehicle has been deleted


def test_create_vehicle_invalid_json():
    response = client.post("/vehicle", json={
        "vin": "6789012345",
        "manufacturer_name": "Honda",
        # Missing required fields
    })
    assert response.status_code == 422  # Unprocessable Entity due to missing required fields
    assert "detail" in response.json()

def test_get_vehicle_invalid_vin():
    response = client.get("/vehicle/INVALIDVIN")
    assert response.status_code == 404  # Vehicle should not exist
    assert "detail" in response.json()
