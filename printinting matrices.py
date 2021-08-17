def print_mat(mat2):
    for i in range(len(mat2)):
        print("│" ,end =' ')
        for j in range(len(mat2[0])):
            print("%4d" %mat2[i][j], end=' ')
        print("│")
    return 0