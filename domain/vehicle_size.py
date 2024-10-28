class VehicleSize:
    SMALL_VEHICLES = [
        "Compact Cars", "Coupe", "Crossover", "Hatchback",
        "Mini Compact Cars", "Subcompact Cars", "Two Seaters",
        "Small Pickup Trucks", "Small Sport Utility Vehicles", "Small Station Wagons"
    ]

    MEDIUM_VEHICLES = [
        "Convertible", "Midsize Cars", "Midsize Station Wagons",
        "Pickup", "Roadster", "Sedan", "Station Wagon", "SUV",
        "Sport Utility Vehicles", "Passenger Vans", "Panel Van"
    ]

    LARGE_VEHICLES = [
        "Cargo Vans", "Large Cars", "Minivan",
        "Standard Pickup Trucks", "Standard Sport Utility Vehicles", "Van"
    ]

    @classmethod
    def get_vehicle_size(cls, vehicle_type: str):
        match vehicle_type:
            case vehicle if vehicle in cls.SMALL_VEHICLES:
                return "small"
            case vehicle if vehicle in cls.MEDIUM_VEHICLES:
                return "medium"
            case vehicle if vehicle in cls.LARGE_VEHICLES:
                return "large"
            case vehicle if vehicle is None:
                return None
            case _:
                raise ValueError(f"Size not found for vehicle {vehicle_type}")

        