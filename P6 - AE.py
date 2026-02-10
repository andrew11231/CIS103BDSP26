#Andrew Espinoza
print('\n'*2)
ans = 'y'

while((ans == 'y') or (ans =='Y')):
    print('Calorie Table Program')
    runmin = float(input('Enter Running Minutes: '))
    cal = 4.33
    minu = 5
    if (runmin == ""  or runmin < 5):
        print('Minutes must be equal or greater than 5')
        ans = input('again y/n: ')
    elif ( runmin > 5):
        while(minu < runmin + 1):
            print('minutes:',minu, 'calories: ',cal * minu)
            minu = minu + 5
        ans = input('again y/n: ')
