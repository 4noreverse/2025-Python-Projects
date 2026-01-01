x, y, z = input('Expression: ').split()
x = int(x)
z = int(z)
if y == '/':
    print(float(x / z))
if y == '+':
    print(float(x + z))
if y == '-':
    print(float(x - z))
if y == '*':
    print(float(x * z))



