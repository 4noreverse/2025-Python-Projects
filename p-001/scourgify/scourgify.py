import os
import sys
import csv
x = len(sys.argv)
total = []
file = sys.argv[1]
out = sys.argv[2]
if x == 3:
    if os.path.exists(sys.argv[1]):
        with open(file, 'r+') as f:
            daread = csv.DictReader(f)
            for i in daread:
                name = i['name']
                house = i['house']
                last, first = name.split(',')
                first = first.strip()
                last = last.strip()
                house = house.strip()
                total.append({'first': first, 'last': last, 'house': house})

        with open(sys.argv[2], 'w') as output:
            fieldname = ['first', 'last', 'house']
            writer = csv.DictWriter(output, fieldnames = fieldname)
            writer.writeheader()
            writer.writerows(total)







    else:
        sys.exit(1)




else:
    sys.exit(1)
