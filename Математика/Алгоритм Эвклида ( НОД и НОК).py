# используется чтобы найти наибольший общий делитель двух чисел
#

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# наименьшее общее кратное
def lcm(a, b):
    return a / gcd(a, b) * b


def test():
    print(gcd(15, 24) == 3)
    print(gcd(7, 14) == 7)
    print(gcd(14, 7) == 7)
    print(gcd(15, 28) == 1)

    print(lcm(15, 24) == 120)
    print(lcm(7, 14) == 14)
    print(lcm(14, 7) == 14)
    print(lcm(15, 28) == 15 * 28)


test()