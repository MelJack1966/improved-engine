'''
Melissa McCormack
CSCI 1060 02
Description: This program converts dollars into Euro or Euro in British pound
depending on user input.
'''

def dtoe():
    dollar = float(input('Enter Dollar Amount: '))
    euro = 0.81*dollar
    print(dollar, 'US Dollar is ', euro, ' Euro')

def etop():
    euro = float(input('Enter Euro Amount: '))
    pound = 0.87*euro
    print(euro, 'Euro is ', pound, ' Pound.')

print('This program converts some amount of dollars into Euro or some amount of Euro into British pound /n depending on the choices made by user')
switch = input('Enter dtoe or etop or end: ')
while switch != 'end':
    if switch == 'dtoe':
        dtoe()
        switch = input('Enter dtoe or etop or end: ')
    elif switch == 'etop':
        etop()
        switch = input('Enter dtoe or etop or end: ')
    else:
        print('Invalid option')
        switch = input('Enter dtoe or etop or end: ')
        
