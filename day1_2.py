import sys, math


def get_fuel(n):
    fuel_req = math.floor(n / 3) - 2
    if fuel_req > 0:
        return fuel_req + get_fuel(fuel_req)
    else :
        return 0


with open(sys.argv[1], 'r+') as file:
    rows = file.readlines()
    total_fuel_needed = 0
    for d in rows:
        v = int(d.strip())
        fuel_req = get_fuel(v)
        print(v, fuel_req)
        total_fuel_needed += fuel_req
    print(total_fuel_needed)