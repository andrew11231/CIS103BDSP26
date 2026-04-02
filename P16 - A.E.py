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
         return str(n) + '+' + summ(n-1)

try:
    num = int(input('Enter Number:'))
    if num > 1:
        print(procs(num)+' = '+ summ(num))
    else:
        print('Number must be positive')
except:
    print('Invalid Input Detected')
    
