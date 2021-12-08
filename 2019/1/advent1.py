import math 

def masscalc(mass):
    return(math.floor(mass/3)-2)

def fuelcalc(fuel, fuelsum):
    fuel = masscalc(fuel)
    print(fuel)
    if fuel<=0:
        return fuelsum
    else:
        fuelsum += fuel 
        return (fuelcalc(fuel,fuelsum))



print(masscalc(12))

print(masscalc(14))

print(masscalc(1969))

print(masscalc(100756))

f = open("input","r")
tot_mass = 0
tot_fuel = 0
for row in f:
    tot_mass += masscalc(int(row))
    tot_fuel += fuelcalc(int(row), 0)


print(fuelcalc(1969, 0))
print(fuelcalc(100756, 0))

print(tot_mass)
print(tot_fuel)