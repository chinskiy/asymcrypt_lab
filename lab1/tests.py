import lab1.ps_rand_numb as gen

const = {'0.01': 2.327, '0.05': 1.645, '0.1': 1.281}


def test1(arr):
    hicv, hi21, n = 0, [], len(arr) / 2 ** 8
    for _ in range(256):
        hicv += ((arr.count(_) - n) ** 2) / n
    for _ in const:
        hi21.append((2 * 255) ** 1/2 * const[_] + 255)
    print(round(hicv, 2), "  ", hi21[0], "  ", hi21[1], "  ",  hi21[2])
    chk = 1
    for elem in hi21:
        if hicv > elem:
            chk = 0
            break
    if chk == 1:
        print("pass")
    else:
        print("error")


if __name__ == "__main__":
    g = [gen.BuiitInGener(), gen.LemerGenFirstBits(), gen.LemerGenLastBits(), gen.L20Generator(),
         gen.L89Generator(), gen.GeffeGen(), gen.Librarian(), gen.BBS()]
    st = ["Built in", "Lemer first bit", "Lemer last bit", "L20", "L89", "GeffeGen", "Librarian", "BBS"]
    randnumb = []
    for _ in range(len(g)):
        randnumb.append(g[_].genseq(10000))
    for _ in range(len(g)):
        print(st[_])
        print("test 1")
        test1(randnumb[_])
        print()
