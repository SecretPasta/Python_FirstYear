def chk_sp_col(mat):
    for j in range(1,len(mat)-1):
        if(mat[j][0]>mat[j-1][0] and mat[j][0]>mat[j-1][1] and mat[j][0]>mat[j][1] and mat[j][0]>mat[j+1][1] and mat[j][0]>mat[j+1][0]):
            print("True",mat[j][0])
        else:
            print("False",mat[j][0])
            
    for j in range(1,len(mat)-1):
        if(mat[j][-1]>mat[j-1][-1] and mat[j][-1]>mat[j-1][-2] and mat[j][-1]>mat[j][-2] and mat[j][-1]>mat[j+1][-2] and mat[j][-1]>mat[j+1][-1]):
            print("True",mat[j][-1])
        else:
            print("False",mat[j][-1])
    return 

def chk_sp_row(mat):
    for i in range(1,len(mat[0])-1):
        if(mat[0][i]>mat[0][i-1] and mat[0][i]>mat[1][i-1] and mat[0][i]>mat[1][i] and mat[0][i]>mat[1][i+1] and mat[0][i]>mat[0][i+1]):
            print("True",mat[0][i])
        else:
            print("False",mat[0][i])
            
    for i in range(1,len(mat[0])-1):
        if(mat[-1][i]>mat[-1][i-1] and mat[-1][i]>mat[-2][i-1] and mat[-1][i]>mat[-2][i] and mat[-1][i]>mat[-2][i+1] and mat[-1][i]>mat[-1][i+1]):
            print("True",mat[-1][i])
        else:
            print("False",mat[-1][i])

    return 0

def chk_crnr(mat):
    if(mat[0][0]>mat[0][1] and mat[0][0]>mat[1][1] and mat[0][0]>mat[1][0]):
        print("True",mat[0][0])
    if(mat[-1][0]>mat[-2][0] and mat[-1][0]>mat[-2][-2] and mat[-1][0]>mat[-1][1]):
        print("True",mat[-1][0])
    if(mat[-1][-1]>mat[-1][-2] and mat[-1][-1]>mat[-2][-2] and mat[-1][-1]>mat[-2][-1]):
        print("True",mat[-1][-1])
    if(mat[0][-1]>mat[0][-2] and mat[0][-1]>mat[1][-2] and mat[0][-1]>mat[1][-1]):
        print("True",mat[0][-1])
    return


def chk_inner_sqr(mat):
    for i in range(1,len(mat)-1):
        for j in range(1,len(mat[0])-1):
            if(mat[i][j]>mat[i-1][j-1] and mat[i][j]>mat[i-1][j] and mat[i][j]>mat[i-1][j+1] and mat[i][j]>mat[i][j+1]  and mat[i][j]>mat[i][j-1] and mat[i][j]>mat[i+1][j+1] and mat[i][j]>mat[i+1][j] and mat[i][j]>mat[i+1][j-1]):
                print("True",mat[i][j])
            else:
                print("False",mat[i][j])

def check_mat(matr):
    chk_inner_sqr(matr)
    chk_crnr(matr)
    chk_sp_row(matr)
    chk_sp_col(matr)
    
    return 

def main():
    mat = [[2,3,4,5,6],[6,5,7,4,3],[3,4,9,8,2],[5,4,8,7,6],[1,2,9,5,9]]
    check_mat(mat)   
    return 0

main()
