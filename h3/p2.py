import sys
from sage.structure.factorization.Factorization import factor

def te(n):
    liars = 0
    exp = (n-1)/2
    for a in range(1,n):
        ans = ((a**exp) % n)
        if ((ans == 1) or (ans == (n-1))):
            liars += 1;
            print str(a)+':' +str(ans)+':'+str(factor(a))
    print str(liars)

def se(n):
    liars = 0
    exp = (n-1)/2
    for a in range(1,n):
        ans = ((a**exp) % n)
        if (ans == 1) or (ans-n == -1):
            liars += 1;
    print str(liars)


def me(n):