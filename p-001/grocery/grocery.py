from collections import Counter
glist = []
while True:
    try:
        item = input().strip().casefold()
        glist.append(item)





    except EOFError:
        num = Counter(glist)
        itum = sorted(num.items())
        for x, y in itum:
            print(y, x.upper())
        break
