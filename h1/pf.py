from fractions import gcd

def pF(n):
    for a in range(n):
        for b in range(n):
            match = False
            sucess = []
            notcoprime = []
            notdisshift = []
            permuted = []
            for i in range(n):
                permuted.append((a*i + b) % n)
            shifted = []
            for i in range(n):
                shifted.append((i - permuted[i]) % n)
            repeats = set([x for x in shifted if shifted.count(x) > 1])
            if (len(repeats) == 0 and (gcd(a,n) == 1)):
                print "Success! a,b:" + str((a,b)) + "Shifted:" + str(shifted) + "Permuted:" + str(permuted)
            elif len(repeats) != 0:
                print "FailureR! a,b:" + str((a,b)) + "Shifted:" + str(shifted) + "Permuted:" + str(permuted)
            elif gcd(a,n) != 1:
                print "FailureG! a,b:" + str((a,b)) + "Shifted:" + str(shifted) + "Permuted:" + str(permuted)