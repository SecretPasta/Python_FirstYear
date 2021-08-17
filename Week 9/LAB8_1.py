#The code will find the largest letter in a string of words
#'a' being the smallest and 'z' being the largest ,letter case is irrelevent 

#This function takes the original strings and uses the 'lower' method
#To make all the characters lower case for ease of use.
#The function receives the original string and returns a lowered case string
def lower_case(string):
    l_string = string.lower()
    return l_string

#This function checks the string for letters and returns the index location
#of the first letter, if no letters are present it will print an error message and
#end the program
#The function receives the lower cased string and returns a bool and an index location of the
#first alphabetic character
def check_string(string):
    for i in range(len(string)):
        if(string[i]>='a' and string[i]<='z'):
            return True,i
    print("There are no alphabet letters")
    return False,i

#This function find the index location of the largest letter in the string with the initial
#value being the first letter in the string then it goes letter by letter to check if it's
#a lower case alphabetic letter and if it's bigger than the last stored value
#The function recevies the lower cased string and starting index and returns the index location
#of the largest alphabetical letter 
def Largest(string,start):
    biggest = string[start]
    B = start
    for i in range(start,len(string)):
        if(string[i]>='a' and string[i]<='z'):
            if(string[i]>biggest):
                biggest = string[i]
                B = i
    return B

#This function find the index location of the smallest letter in the string with the initial
#value being the first letter in the string then it goes letter by letter to check if it's
#a lower case alphabetic letter and if it's smaller than the last stored value
#The function recevies the lower cased string and starting index and returns the index location
#of the smallest alphabetical letter 
def Smallest(string,start):
    smallest = string[start]
    S = start
    for i in range(start,len(string)):
        if(string[i]>='a' and string[i]<='z'):
            if(string[i]<smallest):
                smallest = string[i]
                S = i
    return S

#Main function that will call all the functions aboe
def main(string):
    l_string = lower_case(string)
    flag,start = check_string(l_string)
    if(flag): #Will enter the loop if the string has alphabeitcal characters
        B,S = Largest(l_string,start), Smallest(l_string,start)
        print("Largest and Smallest alphabets are: ",string[B],string[S])

main(str(input("Enter your sentance: "))) #Asking the user to enter a string and sending it to 'main'