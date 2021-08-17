#This code will check if a one string is a mirror of another string using recursion

#This function will check the strings by comparing the first letter of the first string 
#to the last letter of the second string and afterwards it will slice out the first letter 
#of the first string and the last letter of the second string and send it to itself.
#The recursion will stop and return False if the lengths of the strings are not matching,or it 
#encounters unmatching letters, and the function will return True if both strings are empty or 
#the final two letters match.
def mirror_chk(string1,string2):
    if len(string1)==0 and len(string2)==0:
        return True
    
    if len(string1)!=len(string2):
        return False

    if len(string1)==1:
        return string1[0]==string2[0]

    if string1[0]!=string2[-1]:
        return False

    return mirror_chk(string1[1:],string2[:len(string2)-1])

#main function to ask for input and check if the strings are a mirror by calling the function
#above and printing a message accordingly
def main():
    string1 =  "abcd"
    string2 =  "dcba"
    if(mirror_chk(string1,string2)):
        print(string1,"is a mirror of",string2)
    else:
        print(string1,"is not a mirror of",string2)
    
    string1 =  "$"
    string2 =  "$"
    if(mirror_chk(string1,string2)):
        print(string1,"is a mirror of",string2)
    else:
        print(string1,"is not a mirror of",string2)

    string1 =  ""
    string2 =  ""
    if(mirror_chk(string1,string2)):
        print(string1,"is a mirror of",string2)
    else:
        print(string1,"is not a mirror of",string2)

    string1 =  "axcd"
    string2 =  "dcba"
    if(mirror_chk(string1,string2)):
        print(string1,"is a mirror of",string2)
    else:
        print(string1,"is not a mirror of",string2)

    string1 =  "xyz123"
    string2 =  "32z1yx"
    if(mirror_chk(string1,string2)):
        print(string1,"is a mirror of",string2)
    else:
        print(string1,"is not a mirror of",string2)
    return 

main ()#calling main