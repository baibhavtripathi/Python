# import sys

# print(sys.argv)
# print(sys.argv[0])

# print('Hi, Officer!')
# parsecs = int(input("Enter number of parsecs: "))
# lightyears = parsecs * 3.26156

# print(str(parsecs) + ' parsecs = ' + str(lightyears) + ' lightyears')

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split(' ')
print(temperatures_list)

print()

template = """Gravity on {name}
-----------------
Planet name: {planet}
Gravity on {name}: {gravity} m/s2"""
print(template.format(name="Ganymede", planet="Mars", gravity="1.34"))

print()

from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time("Mars", 45))

print("\nVariable arguments are stored as tuple\n")

def variable_arguments(*args):
    print(args)

variable_arguments()
variable_arguments(12, "ty")
variable_arguments(None)

print("\nKeyword varaible arguments are stored as dictionary\n")

def keyword_variable_arguments(**kwargs):
    print(f"{len(kwargs)} astronauts flew in Appolo mission.")
    for key, val in kwargs.items():
        print("Role: {} and Name: {}".format(key, val))

keyword_variable_arguments(pilot="Neil Armestrong", commandar="Yuri")

