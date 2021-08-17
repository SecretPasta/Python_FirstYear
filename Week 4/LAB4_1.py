#The code will recieve the hight and weight of the user and return the calculation of BMI
#Will recieve the Weight of the user, will be stored in 'we'
we = int(input("Please enter your weight in [kg]: "))
#Will recive the Height of the user, will be stored in 'he'
he = int(input("Please enter you height in [cm]: "))
#Converting the value in 'he to a float and deviding be 100 to recive height in meters
he = float(he/100)
#'BMI' will recive the calculation of the BMI
BMI = we/(he**2)
if (BMI<18.5):               #If the BMI is under 18.5
    print("Underweight")     #The user will recive the message "Underweight"
elif (18.5<=BMI<25.0):       #If the BMI is between 18.5 and 25.0
    print("Normal Weight")   #The user will recive the message "Normal Weight"
elif (25.0<=BMI<30.0):       #If the BMI is between 25 and 30
    print("Increased Weight")#The user will recive the message "Inceased Weight"
elif (30.0<=BMI<40.0):       #If the BMI is between 30 and 40
    print("Obese")           #The user will recive the message "Obese"
else:                        #The remaining option is a BMI above 40
    print("Very High Obese") #The user will recive the message "Very High Obese"
    
    
