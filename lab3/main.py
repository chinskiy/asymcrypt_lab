import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    n = 2347005242079226945585535196405279375307319571684939560434521515245704053206537350319828098970555162421821707535960272539014025710453184907401513754302736459679249286363266803488719184367178825220178582056894294517735599338195150572605474288894871281310914527972115020844028444314510306643294668802121072659491429527598435534562628279089473697663341431868130680386891826028525526365208807547331635327667208901520451184096803109154406395764740037226808515613857329145649483892184645598080912531929193349792961653785391835618345177442156179708353523189190521013352912268043026782388403515232678185904779540863893887113
    print("n=", n)
    t = random.randint(1, n)
    print("t= ", t)
    y = t * t % n
    print("y= ", y)
    z = int(input("Enter z: "))
    if t == z:
        print("t == z")
        exit()
    else:
        p = gcd(t+z, n)
        print("p= ", p)
        q = n // p
        print("q= ", q)
        print("p*q= ", p * q)