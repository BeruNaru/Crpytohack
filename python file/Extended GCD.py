import math


def egcd(r1, r2, s1, s2, t1, t2):
    if r2 == 0:
        print(f'gcd:{r1}\ns {s1}\nt: {t1}')
        return
    q = r1 // r2
    r = r1 % r2
    s = s1 - q*s2
    t = t1 - q*t2

    return egcd(r2, r, s2, s, t2, t)

egcd(26513, 32321, 1, 0, 0, 1)

#(p * u)+(q * v) = gcd(p,q)
#crypto{10245,-8404} 답 10245 또는 -8404



