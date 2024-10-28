from domain.vehicle import Vehicle
from domain.vehicle_size import VehicleSize


class TestVehicle:
    def setup_method(self):
        self.vehicle_type = "Minivan"
        self.vehicle = Vehicle(2017, "Ford", "Mustang")

    def test_vehicle_attributes_no_size(self):
        assert self.vehicle.year == 2017
        assert self.vehicle.make == "Ford"
        assert self.vehicle.model == "Mustang"
        assert self.vehicle.size is None

    def test_vehicle_attributes_with_size(self):
        vehicle = Vehicle(2017, "Ford", "Mustang")
        vehicle.vehicle_type = self.vehicle_type

        assert vehicle.year == 2017
        assert vehicle.make == "Ford"
        assert vehicle.model == "Mustang"
        assert vehicle.size == "large"

    def test_vehicle_representation_no_size(self):
        expected_string = "<Vehicle 2017 Ford Mustang (None)>"
        assert repr(self.vehicle) == expected_string

    def test_vehicle_representation_with_size(self):
        vehicle = Vehicle(2017, "Ford", "Mustang")
        vehicle.vehicle_type = self.vehicle_type

        expected_string = "<Vehicle 2017 Ford Mustang (large)>"
        assert repr(vehicle) == expected_string
