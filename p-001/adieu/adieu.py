import inflect
p = inflect.engine()
n = 0
namelist = []
while True:
    try:
        name = input('Name: ')
        namelist.append(name)

    except EOFError:
        print()
        break


if len(namelist) == 1:
    print(f'Adieu, adieu, to {name}')
else:
    joe = p.join((namelist), sep=',', sep_spaced=True, conj='and')
    print(f'Adieu, adieu, to {joe}')
