#Andrew Espinoza
import time
print('\n'*2)
#Name
nam = input('Name: ')
while len(nam) == 0 or nam.isspace() or len(nam) < 3 or not nam.isalpha():    
    if (len(nam) == 0) or nam.isspace():
        print('Name cannot be blank') 
        time.sleep(4)
        nam = input('Name: ')
    elif(len(nam) < 3 ):
        print('Name too short')
        time.sleep(4)
        nam = input('Name: ')
    elif not (nam.isalpha()):
         print('Name must be alphabetic')
         time.sleep(4)
         nam = input('Name: ')
    else:
        break
#Account
print('\n'*2)
acc = input('Account Number:')
while len(acc) == 0 or acc.isspace() or len(acc) != 9 or not acc.isnumeric():
    if (len(acc)==0) or acc.isspace():
        print('Account Number cannot be blank')
        time.sleep(4)
        acc = input('Account Number:')
    elif not (acc.isnumeric()):
        print('Account Number must be numeric')
        time.sleep(4)
        acc = input('Account Number:')
    elif not(len(acc) == 9):
        print('Account Number must be 9 digits')    
        time.sleep(4)
        acc = input('Account Number:')
    else:
        break
    
#Payment    
print('\n'*2)
paym = input('Payment:')
while len(paym) == 0 or paym.isspace() or not paym.isnumeric() or float(paym) <=0:
    if (len(paym)==0) or paym.isspace():
        print('Payment cannot be blank')
        time.sleep(4)
        paym = input('Payment:')
    elif not (paym.lstrip('-').isnumeric()):
         print('Payment must be numeric')
         time.sleep(4)
         paym = input('Payment:')
    else:
        pay = float(paym)
        if (pay <= 0):
            print('Payment cannot be zero or below zero')
            time.sleep(4)
            paym = input('Payment:')
        else:
            break
    
  
print('\n')
print('Thank you for your payment')
