item = str(input())

def convert(item):
    if ':)' in item and ':(' in item:
        both = item.replace(':)', '🙂').replace(':(', '🙁')
        return both
    elif ':)' in item:
        smiley = item.replace(':)', '🙂')
        return smiley
    elif ':(' in item:
        frowney = item.replace(':(', '🙁')
        return frowney

def main(item):
    return convert(item)

print(main(item))

