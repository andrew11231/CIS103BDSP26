#Andrew Espinoza
print('\n'*2)
print('Conversion Program')
print('\n'*2)
anss = 'y'
def convert(x):
    if(x=='a'):
        try:
            acres = float(input('Enter Acres: '))
            hect = acres * 0.4047
            print(acres, ' converts to',hect," hectares")
        except(TypeError,ValueError):
            print('Input error - acres')
            print('--------------')
    elif(x=='q'):
        try:
                quarts = float(input('Enter quarts: '))
                lit = quarts * 0.946353
                print(quarts, ' converts to',lit," liters")
        except(TypeError,ValueError):
                print('Input error - quarts')
                print('--------------')
    elif(x=='f'):
        try:
             fah = float(input('Enter Fahrenheit: '))
             kel = (fah -32)*(5/9)+273.15
             print(fah, ' converts to',kel," kelvin")
        except(TypeError,ValueError):
             print('Input error - acres')
             print('--------------')

while (anss == 'y') or (anss == 'Y'):
    convert('a')
    convert('q')
    convert('f')
    anss = input('again y/n? :')
        