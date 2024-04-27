"""
Karatsuba multiplication algorithm
"""

def karatsuba(x, y):
    # base case: if the input numbers are single digits, 
    # perform simple multiplication and return the result
    if x < 10 or y < 10:
        return x * y

    # determine the number of digits
    x_str = str(x)
    y_str = str(y)
    n = max(len(x_str), len(y_str))

    # split the numbers into halves
    m = n // 2
    fst1, snd1 = divmod(x, 10**m)
    fst2, snd2 = divmod(y, 10**m)

    # recursively apply the karatsuba algorithm on the halves
    z0 = karatsuba(snd1, snd2)
    z1 = karatsuba((snd1 + fst1), (snd2 + fst2))
    z2 = karatsuba(fst1, fst2)

    # compute the final result using karatsuba formula
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0


# test
# case 1
# x = 1234
# y = 5678
# ans = 7006652
# print("Karatsuba multiplication of", x, "and", y, ":", karatsuba(x, y))

# case 2
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
ans = 85397342226735670654635508695465744950348885357651149618796011
27067743044893204848617875072216249073013374895871952806582723184
print("Karatsuba multiplication of", x, "and", y, ":", karatsuba(x, y))

