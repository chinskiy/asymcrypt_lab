import random
import time
import lab1.ps_rand_numb as gener


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def get_prime_number(length):
    while True:
        numb = int(gener.BBSbyte().genseqbin(length), 2)
        if make_test(numb) == 0:
            continue
        return numb


def test_trial_divisions(numb):
    arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    for _ in arr:
        if numb % _ == 0:
            return 0
    return 1


def mil_rab_test(p, k):
    q = (p - 1) // 2
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


def make_test(numb):
    if test_trial_divisions(numb) == 0:
        return 0
    if mil_rab_test(numb, 15) == 0:
        return 0
    return 1


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


def gener_sofi_seng_numb(leng):
    while True:
        tmp = get_prime_number(leng)
        for _ in range(1, 1000):
            if make_test(2 * tmp * _ + 1) == 1:
                return tmp


def gener_pq(leng):
    return gener_sofi_seng_numb(leng), gener_sofi_seng_numb(leng // 2)


def build_rsa(leng):
    p, q = gener_pq(leng)
    n, phi, e = p * q, (p - 1) * (q - 1), 2 ** 16 + 1
    d = modinv(e, phi)


if __name__ == "__main__":
    build_rsa(256)