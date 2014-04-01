import math



def karadec(x,y):
    print(str([x,y]))
    if int(x) < 10 or int(y) < 10:
        return int(x*y)
    m = max(len(str(x)),len(str(y)))
    m2 = math.ceil(m/2)
    [x1,x0] = [int(str(x)[:m2]),int(str(x)[m2:])]
    [y1,y0] = [int(str(y)[:m2]),int(str(y)[m2:])]
    [z0,c0] = karadec(x0,y0)
    print("Z0"+str(z0))
    [z2,c2] = karadec(x1,y1)
    print("Z2 "+str(x1)+ " " +str(y1))
    [z1,c1] = karadec(int(x0+x1),int(y0+y1))
    z1 = z1  - z2 - z0
    print("Z1"+str(z1))
    return z2*10**(2*m2)+z1*(10**m2)+z0
