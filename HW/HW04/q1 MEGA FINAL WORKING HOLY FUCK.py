#This code will check if each cell is bigger than all its neighbours and print out all these cells with the coordinates of the cell

#This function will check the far right and far left columns of the matrix and print out everytime it ecnounters a cell matching the description
def chk_sp_col(mat,count):
    for j in range(1,len(mat)-1):
        if(mat[j][0]>mat[j-1][0] and mat[j][0]>mat[j-1][1] and mat[j][0]>mat[j][1] and mat[j][0]>mat[j+1][1] and mat[j][0]>mat[j+1][0]):
            count+=1
            print(count, end = '')
            print(". mat[",j,"][ 0 ] = ",mat[j][0], ">", mat[j-1][0],mat[j-1][1],mat[j][1],mat[j+1][1],mat[j+1][0])
                    
    for j in range(1,len(mat)-1): 
        if(mat[j][-1]>mat[j-1][-1] and mat[j][-1]>mat[j-1][-2] and mat[j][-1]>mat[j][-2] and mat[j][-1]>mat[j+1][-2] and mat[j][-1]>mat[j+1][-1]):
            count+=1
            print(count, end = '')
            print(". mat[",j,"][",len(mat[0])-1,"] = ",mat[j][-1], ">", mat[j-1][-1],mat[j-1][-2],mat[j][-2],mat[j+1][-2],mat[j+1][-1])  
             
    return count
#This function will check the top and bottom rows of the matrix and print out everytime it ecnounters a cell matching the description
def chk_sp_row(mat,count):
    for i in range(1,len(mat[0])-1):
        if(mat[0][i]>mat[0][i-1] and mat[0][i]>mat[1][i-1] and mat[0][i]>mat[1][i] and mat[0][i]>mat[1][i+1] and mat[0][i]>mat[0][i+1]):
            count+=1
            print(count, end = '')
            print(". mat[ 0 ][",i,"] = ",mat[0][i], ">", mat[0][i-1],mat[1][i-1],mat[1][i],mat[1][i+1],mat[0][i+1])
             
    for i in range(1,len(mat[0])-1):
        if(mat[-1][i]>mat[-1][i-1] and mat[-1][i]>mat[-2][i-1] and mat[-1][i]>mat[-2][i] and mat[-1][i]>mat[-2][i+1] and mat[-1][i]>mat[-1][i+1]):
            count+=1
            print(count, end = '')
            print(". mat[",len(mat)-1,"][",i,"] = ",mat[-1][i], ">", mat[-1][i-1],mat[-2][i-1],mat[-2][i],mat[-2][i+1],mat[-1][i+1])
        
    return count

#this function will check the corners of the matrix and print out everytime it ecnounters a cell matching the description
def chk_crnr(mat,count):
    if(mat[0][0]>mat[0][1] and mat[0][0]>mat[1][1] and mat[0][0]>mat[1][0]):
        count+=1
        print(count, end = '')
        print(". mat[ 0 ][ 0 ] = " ,mat[0][0], ">",mat[0][1],mat[1][1],mat[1][0])  
        
    if(mat[-1][0]>mat[-2][0] and mat[-1][0]>mat[-2][-2] and mat[-1][0]>mat[-1][1]):
        count+=1
        print(count, end = '')
        print(". mat[",len(mat)-1, "][ 0 ] = " ,mat[-1][0], ">",mat[-2][0],mat[-2][-2],mat[-1][1])
        
    if(mat[-1][-1]>mat[-1][-2] and mat[-1][-1]>mat[-2][-2] and mat[-1][-1]>mat[-2][-1]):
        count+=1
        print(count, end = '') 
        print(". mat[",len(mat)-1, "][", len(mat[0])-1,"] = " ,mat[-1][-1], ">",mat[-1][-2],mat[-2][-2],mat[-2][-1])
         
    if(mat[0][-1]>mat[0][-2] and mat[0][-1]>mat[1][-2] and mat[0][-1]>mat[1][-1]):
        count+=1
        print(count, end = '')        
        print(". mat[ 0 ][", len(mat[0])-1,"] = " ,mat[0][-1], ">",mat[0][-2],mat[1][-2],mat[1][-1])
    return count
 
#This function will check the cells in the inner square of the matrix and print out everytime it ecnounters a cell matching the description
def chk_inner_sqr(mat,count):
    for i in range(1,len(mat)-1):
        for j in range(1,len(mat[0])-1):
            if(mat[i][j]>mat[i-1][j-1] and mat[i][j]>mat[i-1][j] and mat[i][j]>mat[i-1][j+1] and mat[i][j]>mat[i][j+1]  and mat[i][j]>mat[i][j-1] and mat[i][j]>mat[i+1][j+1] and mat[i][j]>mat[i+1][j] and mat[i][j]>mat[i+1][j-1]):
                count+=1
                print(count, end = '')
                print(". mat[",i,"][",j,"] = " ,mat[i][j],">",mat[i-1][j-1],mat[i-1][j],mat[i][j+1],mat[i-1][j+1],mat[i][j-1],mat[i+1][j-1],mat[i+1][j],mat[i+1][j+1],      )
    return count

#A special case function for a matrix that consists of a single column and print out everytime it ecnounters a cell matching the description
def ver_col(col,count): 
    if(col[0]>col[1]):
        count+=1
        print(count, end = '')
        print(". mat[ 0 ][ 0 ] = " ,col[0][0], ">",col[1][0])
    if(col[-1]>col[-2]):
        count+=1
        print(count, end = '')
        print(". mat[" ,len(col)-1 ,"][ 0 ] = " ,col[-1][0], ">",col[-2][0])
    for i in range(1,len(col)-1):
        if(col[i]>col[i+1] and col[i]>col[i-1]):
            count+=1
            print(count, end = '')
            print(". mat[" ,i,"][ 0 ] = " ,col[i][0], ">",col[i+1][0],col[i-1][0])                
    return count

#A special case function for a matrix that consists of a single row and print out everytime it ecnounters a cell matching the description
def ver_row(row,count):
    if(row[0][0]>row[0][1]):
        count+=1
        print(count, end = '')
        print(". mat[ 0 ][ 0 ] = " ,row[0][0], ">",row[0][1])
    if(row[0][-1]>row[0][-2]):
        count+=1
        print(count, end = '')
        print(". mat[ 0 ][" ,len(row[0])-1 , "] = " ,row[0][-1], ">",row[0][-2])
    for i in range(1,len(row[0])-1):
        if(row[0][i]>row[0][i+1] and row[0][i]>row[0][i-1]):
            count+=1 
            print(count, end = '')
            print(". mat[ 0 ][" ,i, "] = " ,row[0][i], ">",row[0][i+1],row[0][i-1])
     
    return count

#A functions for a single cell matrix, just printing 
def single_cell(cell,count):
    print("Single cell matrix does not have any neighbours")
    print("mat[ 0 ][ 0 ] = ",cell[0][0])
    return 0

#This funcion will call all the functions above to check all the cells in the matrix 
#in addition checking for the special case of a single column matrix or a single row matrix and 
#For a single row matrix to work it must be entered as a list inside of a list. all the functions will also advance a counter to count
#how many cells that fit the description exist and return the result to the main function
def check_mat(matr):
    count = 0
    if(len(matr)==1 and len(matr[0])==1):
        count = single_cell(matr,count)
    elif(len(matr[0])==1):
        count = ver_col(matr,count)
    elif(len(matr)==1):
        count = ver_row(matr,count)
    else:
        count = chk_inner_sqr(matr,count)
        count = chk_crnr(matr,count)
        count = chk_sp_row(matr,count)
        count = chk_sp_col(matr,count)    
    return count

def main():#Main function that defines the matrix and calls the function above as well as print the counter value at the end
    mat = [[2,3,4,5,6],[6,5,7,4,3],[3,4,9,8,2],[5,4,8,7,6],[1,2,9,5,9]]
    mat = [[85]]
    print("count = ",check_mat(mat))   
    return 0
main()#calling main
