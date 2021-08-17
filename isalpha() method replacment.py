def is_alpha(var):
    for i in range(len(var)):
        if not (var[i]>= 'a' and var[i]<= 'z' or var[i]>= 'A' and var[i]<= 'Z' ):
            return False
    return True
