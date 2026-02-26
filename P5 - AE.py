# Andrew Espinoza

print('\n'*2)
print('Table Codes: A = add, S = subtract, M = multiple, D = divide')

tcode = input('Select table code: ')
tnum = float(input('Enter Number for table: '))

if tcode == 'a' or tcode == 'A':
    for z in range(1, 11):
        print(tnum, "+", z, "=", tnum + z)

elif tcode == 's' or tcode == 'S':
    for z in range(1, 11):
        print(tnum, "-", z, "=", tnum - z)

elif tcode == 'm' or tcode == 'M':
    for z in range(1, 11):
        print(tnum, "*", z, "=", tnum * z)

elif tcode == 'd' or tcode == 'D':
    for z in range(1, 11):
        print(tnum, "/", z, "=", tnum / z)

else:
    print('error')
