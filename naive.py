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

def comp(chunk):
    bit1Cnt = count1(chunk)
    truth = []
    for b in chunk:
        truth.extend(list("{:08b}".format(b)))
    truth.append("1")

    data = ["1"] * (bit1Cnt + 1)
    idx = 0
    while data != truth:
        next(data)
        idx += 1

    return bit1Cnt, idx

def decomp(bit1Cnt, idx):
    data = ["1"] * (bit1Cnt + 1)
    for i in range(idx):
        next(data)
    data = data[:-1]
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

    elif cmd == ["c"]: # comp
        for f in sys.argv[2:]:
            chunk = open(f,"rb").read(CHUNK_SIZE)
            start = time.time()
            bit1Cnt, idx = comp(chunk)
            end = time.time()
            et = end - start
            x = math.log(idx) / math.log(2) / len(chunk)
            print(f"{f}: {bit1Cnt} {idx} {x:.6}x #RT={et:.3}s")

    elif cmd == ["d"]: # decomp
        bit1Cnt = int(sys.argv[2])
        idx = int(sys.argv[3])

        start = time.time()
        data = decomp(bit1Cnt, idx)
        end = time.time()
        et = end - start
        print(f"RT={et:.3}s")
        print(data)

    else:
        print("Unknown command", cmd)