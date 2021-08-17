#The code will receive the velocity of an object and the angle of its launch 
#and will calculate its' distance and height every 0.1 seconds

import math #importing math library to use in the code

#Defining a function'deg2rad' that will convert degrees to radians
#the function recieves one value definied 'deg'
def deg2rad(deg):
    rad=deg*(math.pi/180) #'rad' will receive the value of the calculation
    return rad #The function will return the value of 'rad' to the main function

#Defining a function 'height' that will caculate the height of the object at a given moment
#the function recieves one value definied 'vely'
def height(vely):
    H = vely*t-9.81*t**2/2 #'H' will receive the value of the calculation
    return H #The function will return the value of 'H' to the main function

#Defining a function 'horizontal' that will caculate the horizontal distance 
#of the object at a given moment, the function recieves one value definied 'velx'
def horizontal(velx):
    S = velx*t#'S' will receive the value of the calculation
    return S #The function will return the value of 'S' to the main function

while 1: #creating an infinite loop
#Asking the user to enter the velocity and angle of the object
    vel , ang = eval(input("Please enter velocity and angle: "))
    global t #Defining a global varaible 't' to use in multiple functions
    t = 0.1  #Reseting 't' to a value of 0.1
#Checking if any of the values are outside of the required range 
    if(vel>100 or vel<0 or ang>90 or ang<0):
        print("Finish") #If so will print "Finish" to the user
        break #ending the loop
    else:#If the values are within range
#calls the function 'deg2rad' and sends it the value of 'ang' then
#'ang' will recieve the value the function 'deg2rad' returns    
        ang = deg2rad(ang)
        velx = vel*math.cos(ang)#'velx' will recieve the velocity of the object in the X axis
        vely = vel*math.sin(ang)#'vely' will recieve the velocity of the object in the Y axis
        while 1:#An infinite loop
#Calling the function 'horizontal' and sending it the value of 'velx',
#'S' will receive the value 'horizontal' returns
            S = horizontal(velx)
#Calling the function 'height' and sending it the value of 'vely',
#'H' will receive the value 'height' returns
            H = height(vely)
            if(H<=0):#Checking if the object hit the ground or not
                print("Fallen!")#If so printing "Fallen"
                break#Ending the loop
#Printing the string will the time with one numbers after the decimal point, the Distance with 3
#numbers after the decimal point and the height with 3 numbers after the decimal point
            print("Time : %.1f" %t + "[s]  Distance = %.3f"%S + " [m] Height: %.3f"%H + " [m]")
            t+=0.1 #Advancing 't' by 0.1