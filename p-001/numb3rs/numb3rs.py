import re
import sys

def main():
    print(validate(input("IPv4 Address: " )))

def validate(ip):
    octet = r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'
    x = bool(re.search(octet, ip))
    return x


if __name__ == '__main__':
    main()
