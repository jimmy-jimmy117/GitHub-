def num(a, b):
    return range(a, b)

i = 1
for i in num(1, 101):
    if i < 101:
        i += 1
        print(i)