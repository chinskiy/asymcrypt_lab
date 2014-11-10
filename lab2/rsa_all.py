import random
import time
import lab1.ps_rand_numb as gener


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_prime_number(length):
    while True:
        numb = int(gener.BBSbyte().genseqbin(length), 2)
        if test_trial_divisions(numb) == 0:
            continue
        if mil_rab_test(numb, 20) == 0:
            continue
        return numb


def test_trial_divisions(numb):
    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    for _ in arr:
        if numb % _ == 0:
            return 0
    return 1


def mil_rab_test(p, k):
    q, r = divmod(p - 1, 2)
    s, d = 1, q
    while True:
        q, r = divmod(q, 2)
        if r == 1:
            break
        s += 1
        d = q
    for __ in range(k):
        x = random.randint(1, p)
        if gcd(x, p) > 1:
            return 0
        if fastpow(x, d, p) == 1 or fastpow(x, d, p) == -1:
            return 1
        for _ in range(1, s):
            tmp = fastpow(x, d * 2 ** _, p)
            if tmp == -1:
                return 1
            elif tmp == 1:
                return 0
        return 0


def fastpow(t, k, p):
    res = 1
    while k:
        if k & 1:
            res = (res * t) % p
        k >>= 1
        if k == 0:
            break
        t = (t * t) % p
    return res


def pair_generator(leng):
    p = get_prime_number(leng)
    q = get_prime_number(leng)
    return [p, q]


if __name__ == "__main__":
    q = pair_generator(256)
    print(hex(q[0]))