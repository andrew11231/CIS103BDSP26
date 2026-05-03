#Andrew Espinoza

import random

def main():
    ans = 'y'
    print("\n" * 2)
    name = input('Enter your Name: ')
    while ans.lower() == 'y':
        limit = ''
        while limit == '':  
            print("\n" * 15)
            try:
                limit = input('Limit of guesses (press Enter for default 15): ')       
                if limit == '':
                    limit = 15
                else:
                    limit = int(limit)
                    
                if not (1 <= limit <= 50):
                    print('Must be between 1 and 50')
                    print('\n')
                    limit = ''
            except ValueError:
                print('Invalid Input')
                print('\n')
                limit = ''
                
        gesnumber = 0
        n = random.randint(1, 150)
        guess = ''
        geswrg = 0
        while n != guess:
            try:
                guess = int(input('\n'+"Enter an integer from 1 to 150: "))
                if (guess >= 1) and (guess <= 150):
                    gesnumber +=1
                    gesleft = limit - gesnumber
                    
                    if guess == n:
                        print ('\n'*3 +"O M G, We got a winner.",name,'guessed the number!')
                        break
                    elif gesleft  > 0 :
                        print('Guesses Left: ' ,gesleft)
                        print('Guesses Made: ',gesnumber,'\n')
                        if guess < n:
                            print ("Go higher!!")
                        elif guess > n:
                            print ("too high!, try lower")
                    else:
                        print('\n'+'Sorry, the number was ',n ,', but you can play again! ')
                        break 
                else:
                    print('Number must be in the range 1-150')
                    guess = ''
                    geswrg +=1
                    
            except ValueError:
                print('Invalid Input')
                guess = ''
                geswrg +=1
        print('\n'+'Number of error guesses: ',geswrg)
        print('Number of guesses made: ',gesnumber)  
        ans = input('\n'+'Play again? y/n: ')
            
            
main()
