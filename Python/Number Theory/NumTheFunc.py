def powmod(a, n, m):
  #Invariant of loop: b^k * p == a^n
  b = a; k = n; p = 1
  while k > 0:
    if k%2 == 0:
      k //= 2; b = (b*b)%m
    else:
      k -= 1; p = (p*b)%m
  return p



def gcd(m,n):
    a = m; b = n
    while b != 0:
        r = a % b
        a = b; b = r

        # (a,b) = (b,r)

    if a > 0:
        return a
    else:
        return (-a)

#print(gcd(int(input("")),int(input(""))))


def extgcd(m,n):
    (a, b) = (m, n)
    (u1, v1) = (1, 0)
    (u2, v2) = (0, 1)
    while b != 0:
        q = a // b
        r = a % b
        (u1, u2) = (u2, u1 - q*u2)
        (v1, v2) = (v2, v1 - q*v2)
        (a, b) = (b, r)

    if a > 0:
        return (a, u1, v1)
    else:
        return (-a, -u1, -v1)


def invmod(x,m):
    (d, u, v) = extgcd(x,m)
    return u


def pollardRhoFactor(m, x0=2, maxSteps=100000000):
    x = x0
    y = (x0*x0 + 1) % m
    d = gcd(x-y,m)
    s = 1
    while d == 1 and s < maxSteps:
        x = (x*x + 1) % m
        y = (y*y + 1) % m
        y = (y*y + 1) % m
        d = gcd(x - y, m)
    return d

def pollardP1Factor(m, x0=2, upperBorder=100000000):
    b = x0
    d = 1
    for s in range(2, upperBorder):
        b = pow(b, s, m)
        d = gcd(b - 1, m)
        if d != 1 or d == m:
            break
    return d
