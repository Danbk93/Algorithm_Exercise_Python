from fractions import Fraction
T = int(input())
i =1
while T > 0:
    a, b = map(int, input().split(' '))
    f = Fraction(a,b)
    if f.numerator == 1:
        print(f.denominator)

    while f.numerator != 1:
        while i>0:
            if f >= Fraction(1,i+1):
                f = f-Fraction(1,i+1)
                if f.numerator == 1:
                    print(f.denominator)
                i = 1
                break
            i += 1

    T -= 1