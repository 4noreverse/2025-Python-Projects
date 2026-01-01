import re
import sys

def main():
    print(convert(input('Hours: ')))

def convert(s):
    s = s.strip()
    if 'to' not in s:
        raise ValueError
    crank = s.split('to')
    x = re.fullmatch(r'([1-9]|1[0-2])(?::([0-5]\d))?\s([AP]M)$', crank[0].strip())
    y = re.fullmatch(r'([1-9]|1[0-2])(?::([0-5]\d))?\s([AP]M)$', crank[1].strip())
    if not y:
        raise ValueError
    if not x:
        raise ValueError

    hour, minute, am_pm = x.groups()
    hour1, minute1, am_pm1 = y.groups()
    if minute is None:
        minute = '00'
    if minute1 is None:
        minute1 = '00'
    minute = int(minute)
    minute1 = int(minute1)

    if minute >= 60 or minute1 >= 60:
        raise ValueError



    hour = int(hour)
    if am_pm == 'AM' and hour == 12:
        hour = 0
    elif am_pm == 'PM' and hour != 12:
        hour += 12

    if minute1 is None:
        minute1 = '00'
    hour1 = int(hour1)
    if am_pm1 == 'AM' and hour1 == 12:
        hour1 = 0
    elif am_pm1 == 'PM' and hour1 != 12:
        hour1 += 12


    twofourone = f'{hour:02}:{minute:02}'
    twofourtwo = f'{hour1:02}:{minute1:02}'
    return f'{twofourone} to {twofourtwo}'


if __name__ == '__main__':
    main()
