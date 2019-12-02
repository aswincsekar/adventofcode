import sys, math

with open(sys.argv[1], 'r+') as file:
    rows = file.readlines()
    total_fuel_needed = 0
    for d in rows:
        v = int(d.strip())
        fuel_req = math.floor(v/3)-2
        print(v, fuel_req)
        total_fuel_needed += fuel_req
    print(total_fuel_needed)