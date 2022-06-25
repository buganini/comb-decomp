
from math import comb # python 3.8+

def decomp(chunk):
    length = len(chunk)
    data = []
    for b in chunk:
        data.extend(list("{:08b}".format(b)))
    l = len(data)

    bit1Cnt = data.count("1")
    idx = 0
    bc = bit1Cnt

    p = l - 1
    while p >= 0:
        if data[p]!="0":
            idx += comb(p, bc)
            bc -= 1
        p -= 1

    return length, bit1Cnt, idx

def comp(length, bit1Cnt, idx):
    data = ["0"] * (length * 8)
    p = len(data) - 1
    bc = bit1Cnt
    while idx > 0:
        c = comb(p, bc)
        if idx >= c:
            data[p] = "1"
            bc -= 1
            idx -= c
        p -= 1
    data = [int("".join(data[i*8:i*8+8]),2) for i in range(len(data)//8)]
    data = bytearray(data)
    return data

if __name__=="__main__":
    CHUNK_SIZE = 3

    import sys
    import time
    import math
    cmd = sys.argv[1:2]

    if cmd == ["d"]: # decomp
        for f in sys.argv[2:]:
            chunk = open(f,"rb").read(CHUNK_SIZE)
            start = time.time()
            length, bit1Cnt, idx = decomp(chunk)
            end = time.time()
            et = end - start
            x = (len(chunk)*8) / math.log(idx, 2)
            print(f"{f}: {length} {bit1Cnt} {idx} {x:.6}x #{et:.3}s")

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