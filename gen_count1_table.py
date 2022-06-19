tbl = []

for i in range(256):
    s = "{:b}".format(i)
    tbl.append(s.count("1"))

print(tbl)