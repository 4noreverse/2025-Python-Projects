def main():
    while True:
         try:
          fraction = input('Fraction: ')
          percent = convert(fraction)
          print(gauge(percent))
          break
         except(ValueError, ZeroDivisionError):
             continue

def convert(fraction):
     x, y = fraction.split('/')
     x = int(x)
     y = int(y)

     if x < 0:
          raise ValueError
     if x > y:
          raise ValueError
     if y == 0:
          raise ZeroDivisionError

     percent = round((x / y) * 100)
     return percent


def gauge(percent):
     if percent <= 1:
          return 'E'
     elif percent >= 99:
          return 'F'
     else:
          return f'{percent}%'


if __name__ == "__main__":
    main()
