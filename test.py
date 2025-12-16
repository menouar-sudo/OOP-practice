from ood import *

veco = Vehicle("Toyota", "123-ALG", 2022)
service1 = Service("tiers", 3000)
record = ServiceRecord(veco, service1, "2025-11-10")

#print(record.summary())
car = Car( "Toyota","123-AB", 2020, 4)
service2 = Service("Oil Change", 5000)
record1 = ServiceRecord(car, service2, "2025-01-10")
record2 = ServiceRecord(car, service1, "2025-01-10")
garage = Garage("AutoFix")

garage.add_record(record1)
garage.add_record(record)
garage.add_record(record2)
garage.get_history()
garage.total_revenue()
garage.list_services_by_vehicle("123-AB")