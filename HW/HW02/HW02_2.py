#The code will receive a list of number and shift it by one digit circlarly to the left

#This function will create an empty array the size decided by the user
#and fill it with numbers from the user
#The function receives the amount of numbers and returns a list
def fill_array(elements):
    array = [0]*elements
    for i in range(elements): 
        array[i] = int(input(f"Enter element {i+1}: "))
    print("Original Array: ",array)
    return array

#Creates a list of the consisting of the left digit of each number in the list
#It does so by taking each number and deviding it by 10 until 1 digit is left
#Additnaly it counts how many devisions were performed and stores it in a seprate list
#to be used later on
#The function receives this list 'Arr' and 'elements' and returns the 'L_D' & 'dev' lists
def Left_Digit(L_Arr,elements):
    L_D = [0]*elements
    dev = [0]*elements
    for i in range(elements):
        temp = L_Arr[i]
        while(temp>10):
            temp = int(temp/10)
            dev[i]+=1
        L_D[i]=temp   
    return L_D,dev

#This function will delete the left digit of each number in the array
#It does so by taking numbers from 'L_D_Arr' multiplying it by 10 to the power of the devision
#amount and subtracts it from the original number.
#if the user entered a single digit number than it will simple put 0 in the new list
#The function receives the lists 'array','Dev',L_D_Arr and elements and returns a list
def Left_Digit_Delete(Array,elements,Dev,L_D_Arr):
    for i in range(elements): 
        if(Array[i]<10):
            t_final = 0
        else: 
            t_final = Array[i]-L_D_Arr[i]*(10**Dev[i])
        Array[i] = t_final
    return Array

#this function will perform the final action of putting each left digit on the right 
#of the number in the cell to the left and the first L_D will be placed in the last cell
#Doing it by multiplying each cell by 10 and adding the L_D value
#the function receives the 'Arr' and 'L_D' lists as well as elements 
#and returns the shifted list
def Shifting(Arr,L_D,elements):
    L_D.append(0)
    for i in range(elements):
        Arr[i]=(Arr[i]*10)+L_D[i+1]
    Arr[-1]=Arr[-1]+L_D[0]
    return Arr

#This function will call all the functions above and print the final shifted list
#this function receives the "Array" list and elements and returns nothing
def left_circular_shift(Array,elements):
    L_D_Arr,Dev=Left_Digit(Array,elements)
    After_Delete = Left_Digit_Delete(Array, elements,Dev,L_D_Arr)
    Final = Shifting(After_Delete,L_D_Arr,elements)
    print("Shifted Array: ",Final)
    return 0

#Asking the user to enter the nubmer of elements
elements = int(input("Enter number of elements: "))
#Calling the 'fill_array function", sending the value of 'elements to it,
# the returned list will be stored in 'Array'
Array = fill_array(elements) 
#Calling the 'left_circular_shift' function and sending the the 'Array' list and value of elements
left_circular_shift(Array,elements)
