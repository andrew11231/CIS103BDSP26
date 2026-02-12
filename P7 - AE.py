#Andrew Espinoza
def dist():
    mil = float(input('Miles: '))
    klm = mil * 1.609344
    print('Distance in Kilometers: ',klm)
def wght():
    pnds = float(input('Pounds: '))
    kg = pnds *  0.45359237
    print('Weight in kilograms: ',kg)
def tempp():
    fare = float(input('Fahrenheit: '))
    cels = (fare - 32) * 5/9
    print('Temperature in Celsius: ',cels)
print('\n'*2)
dist()
print('\n'*2)
wght()
print('\n'*2)
tempp()
print('\n'*2)
