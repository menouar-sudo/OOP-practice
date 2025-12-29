from main import *

def test_object_car():#same as Vehicle and Truck
    audi = Car("Audi R8", "25584-225-16", 2025, 4)
    assert audi.brand == "Audi R8"
    assert audi.plate_number == "25584-225-16"
    assert audi.year == 2025
    assert audi.number_of_doors == 4
    assert audi.get_info() == "This is a Audi R8 car, with plate id :25584-225-16, year:2025, with 4 doors."
#test service
    service1 = Service("tiers", 3000)
    assert service1.service_name == "tiers"
    assert service1.get_price() == 3000
#test serviceRecord
    record1 = ServiceRecord(audi, service1, "2025-01-10")
    assert record1.vehicle == audi
    assert record1.service == service1
    assert record1.date == "2025-01-10"
    assert record1.summary() ==('Audi R8', '25584-225-16', 2025, 'tiers', '2025-01-10', 3000)
#test garage
    garage = Garage("AutoFix")
    assert garage.name == "AutoFix"
    assert garage.history == []
#test service record
    garage.add_record(record1)
    assert garage.history == [('Audi R8', '25584-225-16', 2025, 'tiers', '2025-01-10', 3000)]
    assert garage.get_history() == print ('Audi R8', '25584-225-16', 2025, 'tiers', '2025-01-10', 3000)
    assert garage.total_revenue() == print("3000")
    assert garage.list_services_by_vehicle("25584-225-16") == print("'Audi R8', '25584-225-16', 2025, 'tiers', '2025-01-10', 3000")

