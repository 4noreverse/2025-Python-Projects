#year month day

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    year = None
    month = None
    day = None
    date = input('Date: ').strip().casefold()

    try:

        if ',' in date:

            m, y = [d.strip() for d in date.split(',')]
            name, x = m.split(' ', 1)
            name = name.title()
            month = months.index(name) + 1
            day = int(x)
            year = int(y)



        elif '/' in date:

            new = date.split('/')
            year = int(new[2])
            month = int(new[0])
            day = int(new[1])

        else:
            continue
        if not (year is not None and month is not None and day is not None):
            continue
        if not 1 <= month <= 12:
            continue
        if not 1 <= day <= 31:
            continue

        print(f'{year:02}-{month:02}-{day:02}')
        break

    except (ValueError, IndexError):
        continue

