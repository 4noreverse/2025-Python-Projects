
felipe = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

running = 0
while True:

    try:
        item = input('Item: ').strip().casefold()
        felipe_low = {k.casefold(): v for k, v in felipe.items()}
        if item not in felipe_low:
            continue
        running = running + felipe_low.get(item.casefold())
        print(f'Total: ${running:.2f}')

    except KeyError:
        break

    except EOFError:
        print()
        break
