'''
This is a system to convert test scores.
Melissa McCormack
'''
c = float(input("Enter number correct here:"))
q = float(input("Enter number of problems here:"))
p = 100
#this line line declares percentage based on inputted decimal with decimal in the hundredth
percent = ((c/q)*p)
print('The score is:', format(percent, '.2f') , '%')
if percent >= 90.00:
    print("Your grade is A")
elif percent >= 80.00:
    print("Your grade is B")
elif percent >= 70.00:
    print("Your grade is C")
elif percent >= 60.00:
    print("Your grade is D")
else:
    print("Your grade is F")
    
