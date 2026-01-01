import re
import sys

def main():
    print(parse(input('HTML: ')))


def parse(s):
    s = s.strip()
    if not re.search(r'youtube\.com/embed/', s):
        return None
    if not s.startswith('<iframe'):
        return None
    x = re.search(r'src=\"([^"]+?)\"', s)
    if not x:
        return None


    url = x.group(1)
    crank = url.split('/')
    value = 'https://youtu.be/' + crank[4]
    return value



if __name__ == '__main__':
    main()
