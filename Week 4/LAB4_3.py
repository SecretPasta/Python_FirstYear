#The code will recieve the number of children, monthly income and if the user served in the military
#And decide if the user is eligable for a mortgage and if he/she is to which plan
#Asking the user for number of children, will be stored in 'Child'
Child = int(input("Please enter number of children: "))
#Asking the user for the monthly salary, will be stored in 'Salary'
Salary = int(input("Please enter monthly income: "))
#Asking the user to input 'y' if he served in the military, will be stored in 'Military'
Military = input("Have you served in the military? \n For Yes enter 'y' , otherwise any other character: ")
#Checking if the user served in the military and has a monthly income of 5000 and above
#Or has 4 or more children and has and a monthly income of 4000 or more
if( ((Military=='y') and (Salary>=5000)) or ((Child>=4) and (Salary>=4000)) ):
##Checking if the user earns more than 7500 a month  in addition to the first 2 conditions  
    if(Salary>7500):
#Printig an approval message with the mortage being 30% of monthly income        
        print("Your Mortgage is approved at the amount of : ",(Salary*0.3))
    else:
#Printig an approval message with the mortage being 20% of monthly income 
        print("Your Mortgage is approved at the amount of : ",(Salary*0.2))
elif(Salary>7500):#Checking if the user earns more than 7500 a month
#Printig an approval message with the mortage being 30% of monthly income 
    print("Your Mortgage is approved at the amount of : ",(Salary*0.3))
else:#If the conditions above are not met than a mortgage is not approved
    print("The Mortgage is not approved.")#Printing the denial message
    
    