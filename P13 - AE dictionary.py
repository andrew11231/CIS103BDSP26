#Andrew Espinoza
ronumerals = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII",
    13: "XIII",
    14: "XIV",
    15: "XV",
    16: "XVI",
    17: "XVII",
    18: "XVIII",
    19: "XIX",
    20: "XX",
    21: "XXI",
    22: "XXII",
    23: "XXIII",
    24: "XXIV"
}

ans = 'y'
while (ans.lower() == 'y'):
    print('\n')
    num = input('type a number:')
    if (len(num)==0) or num.isspace():
        print('it cannot be blank')
    elif num[0]=='-':
        print('number cannot be negative')
        print('\n')
        ans = 'n'
        print(ronumerals)
    elif not num.isnumeric():
        print('it has to be numeric')
    else:
        try:
            num = int(num)
            if num <= 0:
                ans = 'n'
                print('number cannot be negative or zero')
            elif num in ronumerals:
                print('The number',num,'is',ronumerals.get(num),'in roman numeral')
            elif num not in ronumerals:
                quest = input('Add to dictionary? y/n:')
                if quest.lower() == 'n':
                    print('Number not added')
                    #Adding to dictionary
                elif quest.lower() == 'y':
                    newnum = num
                    newrom = input('Type the Roman Numeral:')
                    if not (newrom.isalpha()):
                        print('Roman numeral has to be alphabetic')
                    else:
                        newrom = newrom.upper()
                        ronumerals.update({newnum:newrom})
                else:
                    print('wrong answer')
                    ans = 'n'
            print('\n')
            print(ronumerals)                
        except:
            print('\n')
            print('Number cannot be negative or zero')
            ans = 'n'
        print('\n')
        ans =  input('again? y/n:')
