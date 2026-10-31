def inf(start=0):
    c = start
    while True:
        yield c
        c += 1
count = inf(start=1)
for n in count:
    print(n)
    if n >= 7:
        break