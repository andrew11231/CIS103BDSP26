#Andrew Espinoza
import random 

numbers = []


    
def powball():
    while len(numbers) < 5:
        num = random.randint(1, 69)
        num = int(num)
        if num not in numbers:
            numbers.append(num)
        numbers.sort()
            
def megmill():
    while len(numbers) < 5:
        num = random.randint(1, 69)
        num = int(num)
        if num not in numbers:
            numbers.append(num)
        numbers.sort()  
        
def lucklot():
    while len(numbers) < 5:
        num = random.randint(1, 45)
        num = int(num)
        if num not in numbers:
            numbers.append(num)
        numbers.sort()  
        
def lotto():
    while len(numbers) < 6:
        num = random.randint(1, 52)
        num = int(num)
        if num not in numbers:
            numbers.append(num)
        numbers.sort()  
        
def main():
    ans = 'y'
    while ans.lower() == 'y':
        numbers.clear()
        print('\n1. Powerball\n'
            '2. Mega Million\n'
            '3. Lucky Day Lotto\n'
            '4. Lotto\n'
            '\n9. Quit')
        selc = input('\nSelection: #')
        if selc == '1':
            powball()
            print('Powerball Numbers: ', *numbers)
        elif selc == '2':
            megmill()
            print('Mega Million Numbers: ', *numbers)
        elif selc == '3':
            lucklot()
            print('Lucky Day Lotto Numbers: ', *numbers)
        elif selc == '4':
            lotto()
            print('Lotto Numbers: ', *numbers)
        elif selc == '9':
            ans = 'done'
            break
        else:
            print('Wrong selection')
        input('\nHit enter to return to menu')
        ans = 'y'
    
    
main()
