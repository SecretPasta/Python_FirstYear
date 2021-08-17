#This code will remove duplicate letters that appear next to each other in a 
#string

#This fuction will remove duplicate letters from the string by turing checking if two
#neighbouring letters are the same, if not it will add the letter at the index location
#to a new string,if the are the same the function will move on this will skip one letter
#adding another letter to the string to make sure the last letter is added
#The function receives the string and returns the new string
def Dupe_Remover(string):
    string += '0'
    new_string = ''
    for i in range(len(string)-1):
        if(string[i]!=string[i+1]):
            new_string+=string[i]
    return new_string

#main function to call the functions above
def main(string):
    print(Dupe_Remover(string))

#Asking the user to enter a string and sending it to main
main(str(input("Please enter a string: ")))
