def main():
    word = str(input('Input: ')).strip()
    print(shorten(word))

def shorten(word):
    for x in word:
        if x.casefold() in 'aeiou'.casefold():
            word = word.replace(x, '')
    return word


if __name__ == "__main__":
    main()






