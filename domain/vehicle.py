from domain.vehicle_size import VehicleSize


class Vehicle:
    def __init__(self, year:int, make: str, model: str):
        self.make = make
        self.model = model
        self.year = year
        self.vehicle_type = None

    @property
    def size(self):
        return VehicleSize.get_vehicle_size(self.vehicle_type)

    def __repr__(self):
        return f"<Vehicle {self.year} {self.make} {self.model} ({self.size})>"
