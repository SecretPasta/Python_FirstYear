import random

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

def check_mat(mat1,d):
    if(check_rows(mat1,d) ):
        return True
    return False

def print_mat(mat2):
    for i in range(len(mat2)):
        print("│" ,end =' ')
        for j in range(len(mat2)):
            print("%4d" %mat2[i][j], end=' ')
        print("│")
            
    

def main():
    while(1):
        dem = int(input("Enter square matrix dimensions: "))
        if (dem == 0):
            print("Finish")
            break
        print("Enter the entries row wise: ")
        mat = []
        for i in range(dem):
            row = []
            for j in range(dem):
                row.append(random.randint(1,1000))
            mat.append(row)
        #for i in range(dem):
         #   print(mat[i])
        print_mat(mat)    
        if(check_mat(mat,dem) and check_col(mat,dem)):
            print("The matrix is perfect")
        else:
            print("The matrix is not perfect")
            
            
    return 0
        

main()