tbl = []
for i in range(256):
    s = "{:b}".format(i)
    tbl.append(s.count("1"))

def count1(a):
    n = 0
    for b in a:
        n += tbl[b]
    return n

def next(a):
    p = 0
    l = len(a)
    n = 0
    while p<l and a[p]=="0":
        p += 1
    while p<l and a[p]!="0":
        p += 1
        n += 1
    if p==l:
        a.append(None)
    a[p] = "1"
    for i in range(p):
        a[i] = "0"
    for i in range(n-1):
        a[i] = "1"

def gen(n, k):
    a = ["1"] * n
    for i in range(k):
        next(a)
    return a

def a_str(a):
    return "".join(a)

def print_a(a, end="\n"):
    s = a_str(a)
    print(s, end=end)

def decomp(chunk):
    length = len(chunk)
    bit1Cnt = count1(chunk)
    truth = []
    for b in chunk:
        truth.extend(list("{:08b}".format(b)))

    while truth[-1]=="0":
        truth.pop()

    data = ["1"] * bit1Cnt
    idx = 0
    while data != truth:
        next(data)
        idx += 1

    return length, bit1Cnt, idx

def comp(length, bit1Cnt, idx):
    data = ["1"] * bit1Cnt
    for i in range(idx):
        next(data)
    data += ["0"] * (length*8-len(data))
    data = [int("".join(data[i*8:i*8+8]),2) for i in range(len(data)//8)]
    data = bytearray(data)
    return data

if __name__=="__main__":
    CHUNK_SIZE = 3

    import sys
    import time
    import math
    cmd = sys.argv[1:2]

    if cmd == ["enum"]:
        bit1Cnt = int(sys.argv[2])
        num = int(sys.argv[3])
        a = ["1"]*bit1Cnt
        for i in range(num):
            # print("{:20b}".format(i), end=":")
            print_a(a, end=" : ")
            print(i)
            # print_a_r(a, 10)
            next(a)

    elif cmd == ["d"]: # decomp
        for f in sys.argv[2:]:
            chunk = open(f,"rb").read(CHUNK_SIZE)
            start = time.time()
            length, bit1Cnt, idx = decomp(chunk)
            end = time.time()
            et = end - start
            x = (len(chunk)*8) / math.log(idx, 2)
            print(f"{f}: {length} {bit1Cnt} {idx} {x:.6}x #RT={et:.3}s")

    elif cmd == ["c"]: # comp
        length = int(sys.argv[2])
        bit1Cnt = int(sys.argv[3])
        idx = int(sys.argv[4])

        start = time.time()
        data = comp(length, bit1Cnt, idx)
        end = time.time()
        et = end - start
        print(f"RT={et:.3}s")
        print(data)

    else:
        print("Unknown command", cmd)