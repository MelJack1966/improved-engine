'''
Melissa McCormack
CSCI 1060-02
Description: The user inputs three people personal info and address info. Then the program prints out the entered information.
'''

ADD = 1
SEARCH = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#Function for getting personal information
def getPersonalInfo():
#Inputs first name
    personalInfo = {}
    personalInfo['First Name'] = input('Enter first name of the person: ')
#Inputs last name
    personalInfo['Last Name'] = input('Enter last name of the person: ')
#Inputs age
    personalInfo['Age'] = input('Enter age of the person: ')
#Inputs height to list
    personalInfo['Height'] = input('Enter height of the person: ')
#Allows info to be ported
    personalInfo['Street Adress:'] = input('Enter street address of the person: ')
#Inputs city
    personalInfo['City:'] = input('Enter city of the person: ')
#Inputs state
    personalInfo['State:'] = input('Enter state of the person: ')
#Inputs zip code
    personalInfo['Zip Code:'] = input('Enter zip code of the person: ')
    return personalInfo

def getMenu():
#Creates menu
    print()
    print('Person ID and their information')
    print('---------------------------------')
    print('1. Add a new person')
    print('2. Search a person')
    print("3. Change a person's info")
    print('4. Delete a person')
    print('5. Quit program')
    print()
#Allows user input
    choice = int(input('Enter a valid choice: '))
    return choice   

#Main function    
def main():
    staffDict = {}
    choice = 0
    while choice != QUIT:
        choice = getMenu()
        if choice == ADD:
            staffDict['1'] = getPersonalInfo()
            staffDict['2'] = getPersonalInfo()
            staffDict['3'] = getPersonalInfo()
        elif choice == SEARCH:
            personalNumber = input('Enter the personal ID 1, 2, or 3: ')
            print(staffDict.get(personalNumber))
        elif choice == CHANGE:
            personalNumber = input('Enter the personal ID 1, 2, or 3: ')
            update = getPersonalInfo()
            staffDict[personalNumber] = update
        elif choice == DELETE:
            personalNumber = input('Enter the personal ID 1, 2, or 3: ')
            del staffDict[personalNumber]
        else:
            print('Good bye')
            
    
main()
