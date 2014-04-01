from fractions import gcd

def pf(n):
    sucessCount = 0
    for a in range(n):
        match = False
        sucess = []
        notcoprime = []
        notdisshift = []
        permuted = []
        for i in range(n):
            permuted.append((a*i + 2) % n)
        shifted = []
        for i in range(n):
            shifted.append((i - permuted[i]) % n)
        repeats = set([x for x in shifted if shifted.count(x) > 1])
        if (len(repeats) == 0 and (gcd(a,n) == 1)):
            sucessCount += 1
            print "Success! a:" + str((a)) + "Count: " + str(sucessCount)
        elif len(repeats) != 0:
            print "FailureR! a:" + str((a))
        elif gcd(a,n) != 1:
            print "FailureG! a:" + str((a)) 