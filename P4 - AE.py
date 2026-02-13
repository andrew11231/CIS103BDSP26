#Andrew Espinoza
import time
while True:
    print('\n'*2)
    #Name
    nam = input('Name: ')
    if (len(nam) == 0):
        print('Name cannot be blank') 
        time.sleep(4)
    elif(len(nam) < 3 ):
        print('Name too short')
        time.sleep(4)
    elif not (nam.isalpha()):
         print('Name must be alphabetic')
         time.sleep(4)
    else:
        break
#Account
while True:
    print('\n'*2)
    acc = input('Account Number:')
    if (len(acc)==0):
        print('Account Number cannot be blank')
        time.sleep(4)
    elif not (acc.isnumeric()):
        print('Account Number must be numeric')
        time.sleep(4)
    elif not(len(acc) == 9):
        print('Account Number must be 9 digits')    
        time.sleep(4)
    else:
        break
    
#Payment    
while True:
    print('\n'*2)
    paym = input('Payment:')
    if (len(paym)==0):
        print('Payment cannot be blank')
        time.sleep(4)
    elif not (paym.isnumeric()):
         print('Payment must be numeric')
         time.sleep(4)
    else:
        pay = float(paym)
        if (pay <= 0):
            print('Payment cannot be zero or below zero')
            time.sleep(4)
       
        else:
            break
    
  
print('\n')
print('Thank you for your payment')