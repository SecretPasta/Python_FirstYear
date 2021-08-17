#This code will check if an IP address is legal or not

#This funciton turns an integer into a string by replaceing each digit with the
#same digit but in string format and at the end reversing the string
def int_to_str(num):
    string =''
    str_num = ['0','1','2','3','4','5','6','7','8','9']
    if(num==0):
        string+='0'
    while(num>0):
        temp=num%10
        string+=str_num[temp]
        num = num//10
    string = string[::-1]    
    return string

#This fucntion will check number of slots is 4
#The function receives the IP and returns a BOOL
def check_slots(ip): 
    if(len(ip)==4):
        return True
    return False

#This function will check if the all the values of the IP adress are digits
#The function receives the IP and returns a BOOL
def if_digit(ip):
    if(ip[0].isdigit() and ip[1].isdigit() and ip[2].isdigit() and ip[3].isdigit()):
        return True
    return False
#This function checks if the entered IP adress has unnecessary zeros by turing each 
#value to an integer and back to a string
#and comparing it to the original number, if they don't match that means it has extra zeros 
#The function receives the IP and returns a BOOL
def check_zero(ip):
    if(int_to_str(int(ip[0]))==ip[0] and int_to_str(int(ip[1]))==ip[1] and int_to_str(int(ip[2]))==ip[2] and int_to_str(int(ip[3]))==ip[3]):
        return True
    return False

#This function will check if the numbers are within the correct range between 0-255 
#The function receives the IP and returns a BOOL
def check_range(ip):
    if(0<=int(ip[0])<256 and 0<=int(ip[1])<256 and 0<=int(ip[2])<256 and 0<=int(ip[3])<256 ):
        return True
    return False

#This function checks if the IP address is legal. it first splits the IP address numbers into a list
#then it calls all the functions above and if they all return 'True' than the function will return 'True' other wise
#It returs'False
#The function receives the IP and returns a BOOL
def is_legal_ip(IP):
    ip = IP.split('.')
    if(check_slots(ip) and if_digit(ip) and check_zero(ip) and check_range(ip)):
        return True
    return False 

#main funcion to call the function above and print the returned result to the user
def main():
    print(is_legal_ip("192.168.1.1"))
    print(is_legal_ip("125.34.251.43"))
    print(is_legal_ip("001.23.45.123"))
    print(is_legal_ip("125.512.100.xy8"))
    print(is_legal_ip("125.512.."))
    print(is_legal_ip("192.168.0.1"))
main()#Calling main 