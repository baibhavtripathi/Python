loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

parsed_config = {}

for line in loaded_config.split('\n'):
    try:
        parsed_config[line.split('=')[0]] = line.split('=')[1]
    except:
        print('parsing error in line: ', line)

print(parsed_config)


print()


def water_left(number_of_astronauts, water_left, days_left):
    for arg in [number_of_astronauts, water_left, days_left]:
        try:
            arg/10
        except TypeError as err:
            return ('Expected integer data type for arguments but received {}'.format(type(arg)))
    
    daily_water_usage = number_of_astronauts * 11
    total_water_required = daily_water_usage * days_left
    total_water_remains = water_left - total_water_required

    if total_water_remains < 0: raise RuntimeError(f'There is not enough water left for {number_of_astronauts} astronauts, after {days_left} days!')
    return f'Total water left after {days_left} days is: {total_water_remains} liters.'

if __name__ == "__main__":
    print(water_left(5, '45', 7))