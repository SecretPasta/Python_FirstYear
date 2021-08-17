#This function will cut out the first letter untill the string is empty and
#then count how many times the function returns and return the final value to main
def length_of_string(s):
    if(s==''):
        return 0
    return 1 + length_of_string(s[1:])
#main function to call the function above and print the result      
def main():   
    text = "Experimental text to test recursive function."
    print("Length of string:\n%s\n is %d."% (text,length_of_string(text)))
main()#calling main

