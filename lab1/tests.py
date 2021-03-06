import lab1.ps_rand_numb as gen
import time


def get_higr(l):
    const, higr = {'0.01': 2.327, '0.05': 1.645, '0.1': 1.281}, []
    for _ in const:
        higr.append(((2 * l) ** 0.5) * const[_] + l)
    higr.sort()
    return higr


def test1(arr):
    hicv, higr, n = 0, [], len(arr) / 2 ** 8
    for _ in range(256):
        hicv += ((arr.count(_) - n) ** 2) / n
    higr = get_higr(255)
    print(repr(round(hicv, 2)).ljust(15), end='')
    for _ in range(3):
        print(repr(round(higr[_], 2)).ljust(15), end='')
    for elem in higr:
        if hicv > elem:
            print("error")
            return
    print("pass")


def test1b(arr):
    hicv, higr, n = 0, [], len(arr) / 2
    for _ in range(2):
        hicv += ((arr.count(_) - n) ** 2) / n
    higr = get_higr(1)
    print(repr(round(hicv, 2)).ljust(15), end='')
    for _ in range(3):
        print(repr(round(higr[_], 2)).ljust(15), end='')
    for elem in higr:
        if hicv > elem:
            print("error")
            return
    print("pass")


def test2(arr):
    hicv, higr, n, nu, alpha = 0, [], len(arr) // 2, [0 for _ in range(2 ** 8)], [0 for _ in range(2 ** 8)]
    nucv = [[0 for _ in range(2 ** 8)] for __ in range(2 ** 8)]
    for _ in range(len(arr)):
        if _ % 2 == 0:
            nu[arr[_]] += 1
            nucv[arr[_]][arr[_ + 1]] += 1
        else:
            alpha[arr[_]] += 1
    for _ in range(2 ** 8):
        for __ in range(2 ** 8):
            if (nu[_] != 0) and (alpha[__] != 0):
                hicv += (nucv[_][__] ** 2)/(nu[_] * alpha[__])
    hicv = (hicv - 1) * n
    higr = get_higr(255 ** 2)
    print(repr(round(hicv, 2)).ljust(15), end='')
    for _ in range(3):
        print(repr(round(higr[_], 2)).ljust(15), end='')
    for elem in higr:
        if hicv > elem:
            print("error")
            return
    print("pass")


def test2b(arr):
    hicv, higr, n, nu, alpha = 0, [], len(arr) // 2, [0 for _ in range(2)], [0 for _ in range(2)]
    nucv = [[0 for _ in range(2)] for __ in range(2)]
    for _ in range(len(arr)):
        if _ % 2 == 0:
            nu[arr[_]] += 1
            nucv[arr[_]][arr[_ + 1]] += 1
        else:
            alpha[arr[_]] += 1
    for _ in range(2):
        for __ in range(2):
            if (nu[_] != 0) and (alpha[__] != 0):
                hicv += (nucv[_][__] ** 2)/(nu[_] * alpha[__])
    hicv = (hicv - 1) * n
    higr = get_higr(2 ** 2)
    print(repr(round(hicv, 2)).ljust(15), end='')
    for _ in range(3):
        print(repr(round(higr[_], 2)).ljust(15), end='')
    for elem in higr:
        if hicv > elem:
            print("error")
            return
    print("pass")


def test3(arr, r):
    hicv, higr = 0, []
    if len(arr) % r != 0:
        arr[0:len(arr) % r] = []
    nucv, m = [[0 for i in range(2 ** 8)] for _ in range(r)], len(arr) // r
    for _ in range(len(arr)):
        nucv[_ // m][arr[_]] += 1
    nu = [sum(x) for x in zip(*nucv)]
    for i in range(2 ** 8):
        for j in range(r):
            if nu[i] != 0:
                hicv += (nucv[j][i]) ** 2 / (nu[i] * m)
    hicv = len(arr) * (hicv - 1)
    higr = get_higr(255 * (r - 1))
    print(repr(round(hicv, 2)).ljust(15), end='')
    for _ in range(3):
        print(repr(round(higr[_], 2)).ljust(15), end='')
    for elem in higr:
        if hicv > elem:
            print("error")
            return
    print("pass")


def test3b(arr, r):
    hicv, higr = 0, []
    if len(arr) % r != 0:
        arr[0:len(arr) % r] = []
    nucv, m = [[0 for i in range(2)] for _ in range(r)], len(arr) // r
    for _ in range(len(arr)):
        nucv[_ // m][arr[_]] += 1
    print(nucv)
    nu = [sum(x) for x in zip(*nucv)]
    print(nu)
    for i in range(2):
        for j in range(r):
            if nu[i] != 0:
                hicv += (nucv[j][i]) ** 2 / (nu[i] * m)
    print(hicv)
    hicv = len(arr) * (hicv - 1)
    print(hicv)
    higr = get_higr(255 * (r - 1))
    print(repr(round(hicv, 2)).ljust(15), end='')
    for _ in range(3):
        print(repr(round(higr[_], 2)).ljust(15), end='')
    for elem in higr:
        if hicv > elem:
            print("error")
            return
    print("pass")


if __name__ == "__main__":
    # g = [gen.BuiitInGener(), gen.LemerGenFirstBits(), gen.LemerGenLastBits(), gen.L20Generator(),
    #      gen.L89Generator(), gen.GeffeGen(), gen.Librarian(), gen.BBSbit(), gen.BBSbyte()]
    # st = ["Built in", "Lemer first bit", "Lemer last bit", "L20", "L89", "GeffeGen", "Librarian", "BBSbit", "BBSbyte"]
    # for _ in range(len(g)):
    #     t0 = time.time()
    #     randnumb = g[_].genseq(1000000)
    #     print(st[_])
    #     # print("test1: ", end='')
    #     # test1(randnumb)
    #     # print("test2: ", end='')
    #     # test2(randnumb)
    #     # print("test3: ", end='')
    #     test3(randnumb, 40)
    #     print(time.time() - t0)
    #     print()
    g = gen.Fibbon()
    randnumb = g.genseq(100)
    test1b(randnumb)
    test2b(randnumb)
    test3b(randnumb, 4)