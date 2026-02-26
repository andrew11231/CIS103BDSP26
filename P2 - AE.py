# Andrew Espinoza
import math

print('\n'*3)
print('Calculate Area of a Rectangle')
print('\n'*2)

wrec = float(input('Place Rectangle Width: '))
hrec = float(input('Place Rectangle Height: '))
arec = wrec * hrec

print('\n')
input('Press Enter Key to Get the Area')
print('\n')
print('The Area is: ', arec)

print('\n'*3)
print('Calculate Area of a Triangle')
print('\n'*2)

btri = float(input('Place Triangle Base: '))
htri = float(input('Place Triangle Height: '))
atri = (0.5 * btri) * htri

print('\n')
input('Press Enter Key to Get the Area')
print('\n')
print('The Area is: ', atri)

print('\n'*3)
print('Calculate Area of a Circle')
print('\n'*2)

radiuscircle = float(input('Place Circle Radius: '))
acirc = math.pi * math.pow(radiuscircle, 2)

print('\n')
input('Press Enter Key to Get the Area')
print('\n')
print('The Area is: ', acirc)
