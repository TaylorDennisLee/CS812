import math
import time



def karadec(x,y):
    if int(x) < 100 or int(y) < 100:
        return [int(x*y),1]
    m = max(len(str(x)),len(str(y)))
    m2 = math.ceil(m/2)
    [x1,x0] = [int(str(x)[:len(str(x))-m2]),int(str(x)[len(str(x))-m2:])]
    [y1,y0] = [int(str(y)[:len(str(y))-m2]),int(str(y)[len(str(y))-m2:])]
    [z0,c0] = karadec(x0,y0)
    [z2,c2] = karadec(x1,y1)
    [z1,c1] = karadec(int(x0+x1),int(y0+y1))
    z1 = z1  - z2 - z0
    return list([int(z2*(10**(2*m2)))+int(z1*(10**m2))+int(z0),int(c0+c1+c2)])

def sg1():
    one = time.clock()
    karadec(12345,6789)
    two = time.clock()
    print(two-one)

def sg2():
    one = time.clock()
    12345*6789
    two = time.clock()
    print(two-one)

