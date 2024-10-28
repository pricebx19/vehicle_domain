from domain.vehicle_size import VehicleSize
import pytest


class TestVehicleSize:
    def test_valid_size(self):
        vehicle_type = "Minivan"
        assert VehicleSize.get_vehicle_size(vehicle_type) == "large"

    def test_valid_size(self):
        vehicle_type = None
        assert VehicleSize.get_vehicle_size(vehicle_type) == None

    def test_invalid_size(self):
        vehicle_type = "hypercar"

        with pytest.raises(ValueError):
            VehicleSize.get_vehicle_size(vehicle_type)

    def test_size_equality(self):
        vehicle_type1 = "Van"
        vehicle_type2 = "Minivan"

        assert VehicleSize.get_vehicle_size(vehicle_type1) == VehicleSize.get_vehicle_size(vehicle_type2)

    def test_size_inequality(self):
        vehicle_type1 = "Van"
        vehicle_type2 = "SUV"

        assert VehicleSize.get_vehicle_size(vehicle_type1) != VehicleSize.get_vehicle_size(vehicle_type2)
