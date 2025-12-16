# OOP-practice
A Python Object-Oriented application that models a vehicle service garage. The system manages vehicles, services, and service records while demonstrating core OOP principles such as encapsulation, inheritance, polymorphism, composition, and aggregation. Designed for clarity, scalability, and clean architecture.

ood.py contains the class object code, while the test.py file used to test it's functionality.
chatGPT task : 
Here’s a clear, practical OOP task for you — realistic and not trivial 👇
(Difficulty: Junior → Mid level)

🧩 OOD TASK: Vehicle Service Management System
🎯 Objective

Design a Python Object-Oriented system to manage vehicles and their service history.

📋 Requirements
1️⃣ Vehicle (Base Class)

Create a class Vehicle with:

Attributes:

plate_number

brand

year

Methods:

get_info() → returns vehicle info as a string

2️⃣ Specialized Vehicles (Inheritance)

Create two classes that inherit from Vehicle:

Car

Truck

Additional attributes:

Car: number_of_doors

Truck: max_load

Override get_info() to include extra data.

3️⃣ Service (Encapsulation)

Create a Service class:

Attributes:

service_name

price

Make price private

Method:

get_price()

4️⃣ ServiceRecord (Composition)

Create ServiceRecord:

Attributes:

vehicle

service

date

Method:

summary() → returns a readable summary

5️⃣ Garage (Aggregation)

Create a Garage class:

Attributes:

name

records (list of ServiceRecord)

Methods:

add_record(record)

total_revenue()

list_services_by_vehicle(plate_number)

🧠 OOD Concepts You Must Use

✔ Classes & Objects
✔ Inheritance
✔ Encapsulation (private attribute)
✔ Polymorphism (get_info())
✔ Composition & Aggregation

🧪 Example Usage (Expected Behavior)
car = Car("123-AB", "Toyota", 2020, 4)
service = Service("Oil Change", 5000)
record = ServiceRecord(car, service, "2025-01-10")

garage = Garage("AutoFix")
garage.add_record(record)

print(garage.total_revenue())
print(garage.list_services_by_vehicle("123-AB"))

🏁 Deliverables

Python code in one file

Clean class structure

No global variables

Proper method usage

🔥 Bonus (Optional)

Add a Motorcycle class

Add validation (price > 0)

Export service history to CSV

Use @property for price
