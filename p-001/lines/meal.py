def main():
    time = input('What time is it? ').strip()
    newtime = convert(time)
    if 7.00 <= newtime <= 8.00:
        return 'breakfast time'
    elif 12.00 <= newtime <= 13.00:
        return 'lunch time'
    elif 18.00 <= newtime <= 19.00:
        return 'dinner time'
    else:
        return
def convert(time):
    hour, minute = map(int, time.split(':'))
    hour = int(hour)
    minute = int(minute)
    return hour + minute / 60
if __name__ == "__main__":
    print(main())
