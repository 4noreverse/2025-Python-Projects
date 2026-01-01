import sys
import csv
import os
from tabulate import tabulate


yo = len(sys.argv)
file = sys.argv[1]

if yo < 2:
    print('Too few command-line arguments')
    sys.exit(1)
elif yo > 2:
    print('Too many command-line arguments')
    sys.exit(1)
elif not file.endswith('.csv'):
    sys.exit(1)
else:
    if os.path.exists(file):
        with open(file, 'r+') as f:
            x = csv.reader(f)
            rows = list(x)
        print(tabulate(rows, tablefmt = 'grid', headers = 'firstrow'))
    else:
        sys.exit(1)
