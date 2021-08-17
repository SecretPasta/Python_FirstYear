#this code will check if matrix is perfect

#this function will check if each number appears once by summing them, i.e. if  
#each number appears once there can only be one sum and comparing it to the sum
#of all the numbers up to the demension value 
def check_rows(rows,n):
    sum1 = 0
   # sum2 = 0
    while(n!=0):
        sum1+=n
        n-=1
    for i in range(len(rows)):
        if not (sum1==sum(rows[i])):
            return False
    return True

#this function will check if each number appears once by summing them, i.e. if  
#each number appears once there can only be one sum and comparing it to the sum
#of all the numbers up to the demension value 
def check_col(mat1,n):
    sum1 = 0
    while(n!=0):
        sum1+=n
        n-=1
    for i in range(len(mat1)):
        sum2 = 0
        for j in range(len(mat1)):
            sum2+=mat1[j][i]
        if not (sum1 == sum2):
            return False
    return True
#This function will print the matrix
def print_mat(mat2):
    for i in range(len(mat2)):
        print("│" ,end =' ')
        for j in range(len(mat2)):
            print("%4d" %mat2[i][j], end=' ')
        print("│")
    return 0
 
#main function that will ask for matrix demensions and each number in each cell
#and will check if the matrix is perfect and print a message accordingly 
def main():
    while(1):
        dem = int(input("Enter square matrix dimensions: "))
        if (dem<=0):
            print("Finish")
            break
        print("Enter the entries row wise: ")
        mat = []
        for i in range(dem):
            row = []
            for j in range(dem):
                row.append(int(input()))
            mat.append(row)
        print_mat(mat)    
        if(check_rows(mat,dem) and check_col(mat,dem)):
            print("The matrix is perfect")
        else:
            print("The matrix is not perfect")
    return 0
        
main()#calling main