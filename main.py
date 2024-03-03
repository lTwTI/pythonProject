class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.manufacturer.title()} {self.model.title()}'
        return long_name

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back the odometer!")


if __name__ == '__main__':
    print()
