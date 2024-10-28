# tests/test_events.py

from domain.vehicle import Vehicle
from domain.vehicle_size import VehicleSize
from domain.events.vehicle_added_event import VehicleAddedEvent


class TestVehicleAddedEvent:

    def setup_method(self):
        self.vehicle = Vehicle(2020, "Tesla", "Model S")
        self.vehicle.vehicle_type = "SUV"
        self.event = VehicleAddedEvent(self.vehicle)

    def test_event_attributes(self):
        assert self.event.vehicle == self.vehicle

    def test_event_representation(self):
        assert repr(self.event) == f"<VehicleAddedEvent <Vehicle 2020 Tesla Model S (medium)>>"
