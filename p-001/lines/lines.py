import sys

num = len(sys.argv)

if num < 2:
    print('Too few command-line arguments')
    sys.exit(1)
elif num > 2:
    print('Too many command-line arguments')
    sys.exit(1)

filename = sys.argv[1].strip()

if not filename.endswith('.py'):
    sys.exit(1)

count = 0
in_docstring = False

with open(filename, 'r') as f:
    for line in f:
        stripped = line.strip()
        if stripped == '':
            continue
        if stripped.startswith('#'):
            continue
        count += 1
print(count)




