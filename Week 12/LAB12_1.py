#This code will check if two matrices are correct

#this function will check if the sum of a given row is equal to its index
def check_row(row,n):
    sum1 = 0
    for i in range(len(row)):
        sum1+=row[i]
    if(sum1==n):
        return True

    return False

#this function will check if the diagonal line consists of positive numbers
def check_diagonal(mat):
    if(len(mat)<len(mat[0])):
        for i in range(len(mat)):
            if(mat[i][i]<=0):
                return False
            
    elif(len(mat)>len(mat[0])):
        for i in range(len(mat[0])):
            if(mat[i][i]<=0):
                return False
    else:
        for i in range(len(mat)):
            if(mat[i][i]<=0):
                return False
    
    return True

#this funcion will print the matrix 
def print_mat(mat2):
    for i in range(len(mat2)):
        print("│" ,end =' ')
        for j in range(len(mat2[0])):
            print("%4d" %mat2[i][j], end=' ')
        print("│") 

#main function that will check if the matrices are correct and print if they
#are correct or not and will print the matrix with the apropriate message
def main():
    mat1 = [[31,-15,0,-12,-4],[1,1,-3,2,0],[12,-2,4,-23,11],[5,0,3,2,-7],[1,1,0,1,1]]
    mat2 = [[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5]]
    print_mat(mat1)
    flag = True
    for i in range(len(mat1)):
        if not (check_row(mat1[i],i)):
            flag = False
            break
    if (flag and check_diagonal(mat1)):
        print("----The Matrix is correct----\n")
    else:
        print("T---he matrix is not correct---\n")
    print_mat(mat2)    
    flag = True
    for i in range(len(mat2)):
        if not (check_row(mat2[i],i)):
            flag = False
            break
    if (flag and check_diagonal(mat2)):
        print("----The Matrix is correct----\n")
    else:
        print("---The matrix is not correct---\n")
      
    return 0

main()#calling main 