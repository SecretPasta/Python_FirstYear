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
            print(". mat[",j,"][ ",len(mat)-1," ] = ",mat[j][-1], ">", mat[j-1][-1],mat[j-1][-2],mat[j][-2],mat[j+1][-2],mat[j+1][-1])  
             
    return count
 
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
            print(". mat[",len(mat[0])-1,"][",i,"] = ",mat[-1][i], ">", mat[-1][i-1],mat[-2][i-1],mat[-2][i],mat[-2][i+1],mat[-1][i+1])
        
    return count

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
 

def chk_inner_sqr(mat,count):
    for i in range(1,len(mat)-1):
        for j in range(1,len(mat[0])-1):
            if(mat[i][j]>mat[i-1][j-1] and mat[i][j]>mat[i-1][j] and mat[i][j]>mat[i-1][j+1] and mat[i][j]>mat[i][j+1]  and mat[i][j]>mat[i][j-1] and mat[i][j]>mat[i+1][j+1] and mat[i][j]>mat[i+1][j] and mat[i][j]>mat[i+1][j-1]):
                count+=1
                print(count, end = '')
                print(". mat[",i,"][",j,"] = " ,mat[i][j],">",mat[i-1][j-1],mat[i-1][j],mat[i][j+1],mat[i-1][j+1],mat[i][j-1],mat[i+1][j-1],mat[i+1][j],mat[i+1][j+1],      )
    return count

def check_mat(matr):
    count = 0
    count = chk_inner_sqr(matr,count)
    count = chk_crnr(matr,count)
    count = chk_sp_row(matr,count)
    count = chk_sp_col(matr,count)    
    return count

def main():
    mat = [[2,3,4,5,6],[6,5,7,4,3],[3,4,9,8,2],[5,4,8,7,6],[1,2,9,5,9]]
    print("count = ",check_mat(mat))   
    return 0

main()
