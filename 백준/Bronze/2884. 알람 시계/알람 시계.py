h,m = map(int, input().strip().split())
if  m >= 45: 
        m -= 45
        print("{} {}".format(h,m))
        
elif  m < 45 : 
    if h == 0:
        h = h +  23 
        m = m + 60 - 45
        print("{} {}".format(h,m)) 
    elif h > 0 :
        h -= 1
        m = m + 60 - 45
        print("{} {}".format(h,m)) 