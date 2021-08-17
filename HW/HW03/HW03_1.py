#This code will replicate the function of the split method

#This function will split the string according to a specific character
#It does so by creating a new empty list and a temporary string and checking 
#weather each letter matches the character if not it will add it to the temp string
#once it encouters a matching letter it will add the temp string to the new list
#and reset the temp string also skipping the character in the string,
#and it will do it once more for the last string
#The fucntion receives a string and a character and returns the new_string.
def my_split(string,ch):
    new_string = []
    temp = ''
    for i in range(len(string)):
        if(string[i]!=ch):
            temp += string[i]
        else:
            new_string.append(temp)
            temp = ''
    if(temp!=''):
        new_string.append(temp)
    return new_string

#Main fucntion that will call the function above and print the list it returns
def main():
    string = "This is an example of how split works"
    print(my_split(string," "))
    print(my_split(string,"s"))
    print(my_split(string,"x"))
    print(my_split(string,"y"))

    return 0

main()#Calling main