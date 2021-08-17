#This code will receive a string and print every word in the string in a new line
#it will do so until the user enters a blank string(nothing)


#This function turns the string into a list with each cell containing a word
#by using 'split' method and a blank is the seperator for each sub string in the list
#The function recieves a string and returns a list
def lister(string):
    listed = string.split()
    return listed

#this function will print the list of words with each word having a new line
#the function receives the list and returns nothing
def print_list(listed):
    for i in range(len(listed)):
        print(listed[i])    
    return 0

#main function with a infinite loop that will continue unill the user enters nothing
#and call the functions above
def main():
    while(1):
        string = str(input("Please enter a string: "))
#If the user entered an empty string print finish and store the loop/end the code
        if(string == ' '*len(string)):
            print("Finish")
            break
        else:#otherwise call these functions
            listed = lister(string)
            print_list(listed)
        
main()#Calling main function