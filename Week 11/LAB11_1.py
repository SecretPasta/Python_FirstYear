#This code will find the first letter that appears the largest ammount of times

#this function count how many time each letter appears and will create a copy
#list sort it and use the largest value to find the first letter that's most
#common, the function receives a string and returns a letter
def most_common_chr(a):    
    chars = [0]*26
    for i in range(len(a)):
        if (a[i]>= 'a' and a[i]<='z'):
            chars[ord(a[i])-97]+=1
    copy = chars.copy()
    copy.sort()
    if (chars.count(0)==26):
        return -1
    common = chars.index(copy[-1])
    
    return chr(common+97)

#Main function that will run untill 'quit' is entered, will accept strings and
#call the functin above to find the most common letter in it.              
def main():
    while(1):
        string = input("Please enter a string: ")
        if (string == 'quit' or string == 'Quit'):
            print("Finish")
            break
        string = string.lower()        
        print(most_common_chr(string))
    return 0

main() #Calling main