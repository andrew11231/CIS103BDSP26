# Andrew Espinoza

print('\n'*2)
pounds = float(input('Number of Pounds: '))
if pounds < 0:
    print('Error')
elif pounds >= 0 and pounds < 10:
    Disc = 0.00
elif pounds >= 10 and pounds < 100:
    Disc = 0.10
elif pounds >= 100 and pounds < 1000:
    Disc = 0.20
elif pounds >= 1000 and pounds < 10000:
    Disc = 0.30
elif pounds >= 10000:
    Disc = 0.40
gross = pounds * .99
discshow = Disc * gross
amountf = gross - discshow
print('\n'*2)
print('Number of Pounds: ', pounds)
print('Gross Sales: ', gross)
print('Discount: ', discshow)
print('Final Amount: ', amountf)
