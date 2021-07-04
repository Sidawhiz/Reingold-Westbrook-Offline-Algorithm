import math

LEFT_TO_RIGHT = True
RIGHT_TO_LEFT = False

def searchArr(a ,n, mobile):         
    for i in range(n):
        if (a[i] == mobile):
           return i + 1
    return 0       


def getMobile(a, dir ,n):
    mobile_prev = 0
    mobile = 0
    for i in range(n):
        if (dir[a[i]-1] == RIGHT_TO_LEFT and i!=0):
            if (a[i] > a[i-1] and a[i] > mobile_prev):
                mobile = a[i]
                mobile_prev = mobile
  
        if (dir[a[i]-1] == LEFT_TO_RIGHT and i!=n-1):
            if (a[i] > a[i+1] and a[i] > mobile_prev):
                mobile = a[i]
                mobile_prev = mobile
    if (mobile == 0 and mobile_prev == 0):
        return 0
    else:
        return mobile

def printOnePerm(a, dir, n , Li, Li2):
    mobile = getMobile(a, dir, n)
    pos = searchArr(a, n, mobile)
    gray2 = Li2[:][-1]
  
    if (dir[a[pos - 1] - 1] ==  RIGHT_TO_LEFT):
        g = a[pos-1]
        h = a[pos - 2]
        if(g>h):
            gray2 += math.factorial(a[pos-1]-1)
        elif(g<h):
           gray2 -= math.factorial(a[pos-1]-1)
        temp = a[pos - 1]
        a[pos - 1] = a[pos - 2]
        a[pos - 2] = temp   
    elif (dir[a[pos - 1] - 1] == LEFT_TO_RIGHT):
        g = a[pos]
        h = a[pos - 1]
        if(g>h):
            gray2 += math.factorial(a[pos-1]-1)
        elif(g<h):
           gray2 -= math.factorial(a[pos-1]-1)
        temp = a[pos]
        a[pos] = a[pos - 1]
        a[pos - 1] = temp

    for i in range(n):
        if(a[i] > mobile):
            if(dir[a[i] - 1] == LEFT_TO_RIGHT):
                dir[a[i] - 1] = RIGHT_TO_LEFT
            elif(dir[a[i] - 1] == RIGHT_TO_LEFT):
                dir[a[i] - 1] = LEFT_TO_RIGHT
    s1 = list()
    for i in range(n):
        s1.append(a[i]) #print(a[i])
    Li.append(s1)
    Li2.append(gray2)
    return 0    
  
def fact(n):
    res = 1;
    for i in range(1,n+1):
        res = res*i
    return res 

def printPermutation(n , Li , Li2):
    a = [None] * n
    dir = [None] * n
    s1 = list()
    for i in range(n):
        a[i] = i + 1
        s1.append(a[i])
    Li.append(s1)
    Li2.append(0)    
    for i in range(n):
        dir[i] =  RIGHT_TO_LEFT
    for i in range(1,fact(n)):
        printOnePerm(a, dir, n , Li , Li2)
    Z = [x for _, x in sorted(zip(Li2, Li))]
    Li2.sort()
    Li3 = []
    for x in Li2:
        s = list()
        t = n
        for i in range(n):
            y = x//math.factorial(t-1)
            s.insert(0,y) 
            x = x - y*math.factorial(t-1)   
            t = t-1
        Li3.append(s)     
    return Z , Li3

if(__name__ == "__main__"):
    Li = []
    Li2 = []
    z, Li3 = printPermutation(5 , Li , Li2)
    print(z)
    print(Li3)

