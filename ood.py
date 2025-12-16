class Vehicle:
    def __init__(self, brand, plate_number, year):
        self.brand = brand
        self.plate_number = plate_number
        self.year = year
    def get_info(self):
        return f"This is a {self.brand} car, with plate id :{self.plate_number}, year:{self.year}"
class Car(Vehicle):
    def __init__(self, brand,plate_number,  year, number_of_doors):
        super().__init__(brand,plate_number,  year)
        self.number_of_doors = number_of_doors
    def get_info(self):
        return f"This is a {self.brand} car, with plate id :{self.plate_number}, year:{self.year}, with {self.number_of_doors} doors."

class Truck(Vehicle):
    def __init__(self,brand, plate_number,  year, max_load):
        super().__init__(brand,plate_number,  year)
        self.max_load = max_load
    def get_info(self):
        return f"This is a {self.brand} truck, with plate id :{self.plate_number}, year:{self.year}, with maximum load of {self.max_load}"
class Service:
    def __init__(self, service_name, price):
        self.service_name = service_name
        self.__price = price

    def get_price(self):
        return self.__price

class ServiceRecord:
    def __init__(self, vehicle, service, date):
        self.vehicle = vehicle      # Vehicle object
        self.service = service      # Service object
        self.date = date


    def summary(self):
        return (
            self.vehicle.brand,
            self.vehicle.plate_number,
            self.vehicle.year,
            self.service.service_name,
            self.date,
            self.service.get_price()
        )
class Garage:
    def __init__(self, name ):
        self.name = name
        self.history = []

    def add_record(self, record):
        self.history.append(record.summary())
        #return f"on {self.name} : record : {record.summary()} \n"
    def get_history(self):
        for record in self.history:
            print(record)
    def total_revenue(self):
        total = 0
        for record in self.history:
            total += record[5]
        print(total)

    def list_services_by_vehicle(self, plate_number):
        results = []  # create an empty list to store matching records
        for record in self.history:
            if record[1] == plate_number:
                results.append(record)
        print(*results, sep="\n")
