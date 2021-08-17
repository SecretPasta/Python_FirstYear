#The code will print the sum of all uneven numbers of the fibonacci sequence
#up to 400,000
x = 1 #First number in the sequance
y = 1 #Second number in the sequance
sum = x + y #Sum of the first two numbers in the sequnace
while(x<400000 and y<400000): #While the unmbers are unber 400,000 loop these lines
    x = x+y # 'x' will recive the sum of the previous two nubmers
    y = x+y # 'y' will recive the sum of the previous two nubmers
    if(x>=400000 or y>=400000):#if one of the numbers exceed 400,000 exit the loop
        break
    if(x%2==1):#Checking the 'x' is an uneven number
        sum+=x #adding 'x' to the 'sum'
    if(y%2==1):#Checking the 'y' is an uneven number
        sum+=y #adding 'y' to the 'sum'      
print(sum) #Printing the sum

