
from math import comb # python 3.8+

def comp(chunk):
    data = []
    for b in chunk:
        data.extend(list("{:08b}".format(b)))
    data.append("1")
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

    return bit1Cnt-1, idx

def decomp(bit1Cnt, idx):
    pass

if __name__=="__main__":
    CHUNK_SIZE = 3

    import sys
    import time
    import math
    cmd = sys.argv[1:2]

    if cmd == ["c"]: # comp
        for f in sys.argv[2:]:
            chunk = open(f,"rb").read(CHUNK_SIZE)
            start = time.time()
            bit1Cnt, idx = comp(chunk)
            end = time.time()
            et = end - start
            x = math.log(idx) / math.log(2) / len(chunk)
            print(f"{f}: {bit1Cnt} {idx} {x:.6}x #{et:.3}s")

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