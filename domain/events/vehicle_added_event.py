from domain.vehicle import Vehicle


class VehicleAddedEvent:
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def __repr__(self):
        return f"<VehicleAddedEvent {self.vehicle}>"