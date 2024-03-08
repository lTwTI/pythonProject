class Car:
    def __init__(self, manufacturer, model: str, year: int) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) -> str:
        long_name = f'{self.year} {self.manufacturer.title()} {self.model.title()}'
        return long_name

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def increment_odometer(self, miles: int) -> None:
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back the odometer!")


class Battery:
    def __init__(self, battery_size: int = 75) -> None:
        self.battery_size = battery_size

    def describe_battery(self) -> None:
        print(f'This car has a {self.battery_size}-kWh battery.')


class ElectricCar(Car):
    def __init__(self, manufacturer: str, model: str, year: int) -> None:
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
