#Andrew Espinoza

def summ(n):
    if n == 1:
        return 1
    else:
         return n + summ(n-1)
     
def procs(n):
    if n == 1:
        return "1"
    else:
         return str(n) + '+' + procs(n-1)


ans = 'y'
while ans.lower() == 'y':
    try:
            print('\n')
            num = int(input('Enter Number:'))
            if num >= 1:
                print(procs(num)+' = '+ str(summ(num)))
                ans = input('y/n? = ')
            else:
                print('Number must be positive')
    except:
            print('Invalid Input Detected')
