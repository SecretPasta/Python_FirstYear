#This function will check if a list is a palindrome or not using recursion

#this function will check if a list is a palindrome by comparing the first and
#last cells, and will call itself with the first and final cells removed and 
#if all the cells are equal it will return True if it encounters unequal cells
#it will return False immediately .
def is_palindrom(arr):

    if len(arr)==1:
        return True
    
    if len(arr)==2:
        return arr[0]==arr[-1]

    if arr[0]!=arr[-1]:
        return False
    
    return is_palindrom(arr[1:len(arr)-1])

#main function that will ask for input,turn it into a list and call the function
#above to check the list and print a message accordingly,it will run until the
#user whishes to stop trying.
def main():
    nums = input("Please enter numbers seprated by a comma:\n")
    list1 = nums.split(',')
    if(is_palindrom(list1)):
        print("The list is a palindrome")
    else:
        print("The list is not a palindrome") 
    cont = input("Try Again? (y/n): ")
    while (cont=='y'):
        nums = input("Please enter numbers seprated by a comma:\n")
        list1 = nums.split(',')
        if(is_palindrom(list1)):
            print("The list is a palindrome")
        else:
            print("The list is not a palindrome") 
        cont = input("Try Again? (y/n): ")
    print("Finish")
        
    return

main ()#calling main