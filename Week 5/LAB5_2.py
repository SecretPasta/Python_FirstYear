#The code will recieve a starting element, a common ratio and number of elements and show all 
#the numbers in geomatric series up to the integer
n1 = eval(input("Please enter the first Element: ")) #Asking for the first nubmer will be stored in 'n1'
q = eval(input("Please enter common ratio:"))#Asking for common ratio, will be stored in 'q'
n = int(input("Enter an integer:"))#Asking for the last integer in the series, will be stored in 'n'
i = 1 #Defining index 'i' at 1
print("Gemotaric Progression Series: \n")#Pritnting the string and going to the next line
while(i<=n):#While 'i' is smaller or equal to 'n' loop the following lines
    num = n1*(q**(i-1))#num will receive the calculation of the value in the poision 'i' in the series
    print(num , end=' ')#Printing the number and making sure all values are on the same line
    i+=1 #Advancing the index by 1