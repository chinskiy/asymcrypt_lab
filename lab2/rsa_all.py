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
        return 0
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
    e = 2 ** 16 + 1
    return dict(d=modinv(e, (p - 1) * (q - 1)), p=p, q=q, n=p * q, e=e)


def encrypt_rsa(mes, e, n):
    return fastpow(mes, e, n)


def decrypt_rsa(c, d, n):
    return fastpow(c, d, n)


def check_rsa_encr_decr(par, mes):
    print('p ', str(hex(par['p']))[2:])
    print('q ', str(hex(par['q']))[2:])
    print('n ', str(hex(par['n']))[2:])
    print('e ', str(hex(par['e']))[2:])
    print('d ', str(hex(par['d']))[2:])
    print('m ', str(hex(mes))[2:])
    cr = encrypt_rsa(m, par['e'], par['n'])
    print('c', str(hex(cr))[2:])
    mes = decrypt_rsa(cr, par['d'], par['n'])
    print('m ', str(hex(mes))[2:])


def create_rsa_sign(mes, d, n):
    return mes, fastpow(mes, d, n)


def check_rsa_sign(mes, s, e, n):
    if mes == fastpow(s, e, n):
        print('Correct')
    return fastpow(s, e, n)


def create_and_check_rsa_sign(par, mes):
    print('n ', str(hex(par['n']))[2:])
    print('e ', str(hex(par['e']))[2:])
    print('d ', str(hex(par['d']))[2:])
    print('m ', str(hex(mes))[2:])
    s = create_rsa_sign(mes, par['d'], par['n'])
    print('s', str(hex(s[1]))[2:])
    mes = check_rsa_sign(s[0], s[1], par['e'], par['n'])
    print('m ', str(hex(mes))[2:])


def chech_protocol_conf_key_sending(a, b, k):
    print('eA ', str(hex(a['e']))[2:])
    print('nA ', str(hex(a['n']))[2:])
    print('dA ', str(hex(a['d']))[2:])
    print('eB ', str(hex(b['e']))[2:])
    print('nB ', str(hex(b['n']))[2:])
    print('dB ', str(hex(b['d']))[2:])
    print('k  ', str(hex(k))[2:])
    k1 = encrypt_rsa(k, b['e'], b['n'])
    print('k1 ', str(hex(k1))[2:])
    s = create_rsa_sign(k, a['d'], a['n'])
    print('s ', str(hex(s[1]))[2:])
    s1 = create_rsa_sign(s[1], b['e'], b['n'])
    print('s1', str(hex(s1[1]))[2:])
    print('Checking:')
    k = decrypt_rsa(k1, b['d'], b['n'])
    print('k ', str(hex(k))[2:])
    s = decrypt_rsa(s1[1], b['d'], b['n'])
    print('s ', str(hex(s))[2:])
    k = check_rsa_sign(k, s, a['e'], a['n'])
    print('k ', str(hex(k))[2:])

if __name__ == "__main__":
    abon_a, abon_b = build_rsa(256), build_rsa(256)
    if abon_a['p'] * abon_a['q'] > abon_b['p'] * abon_b['q']:
        abon_a, abon_b = abon_b, abon_a
    m = int(gener.BBSbyte().genseqbin(100), 2)
    #check_rsa_encr_decr(abon_a, m)
    #create_and_check_rsa_sign(abon_a, m)
    chech_protocol_conf_key_sending(abon_a, abon_b, m)