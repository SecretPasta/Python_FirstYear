def is_digit(var):
    for i in range(len(var)):
        if not (var[i]>= '0' and var[i]<= '9'):
            return False
    return True
