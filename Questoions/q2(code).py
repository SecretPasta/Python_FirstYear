def f4(s1):
    i,j=0,len(s1)-1
    s2=s3=''
    while i<=j:
        s2+=s1[j]
        if i<j:
            s3 = s1[i]+s3
        i+=1
        j-=1
    return s2+s3

print(f4("FOREVER"))