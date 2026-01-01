def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    forbid = ',!?. '
    numba = s[2:]
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    for i in forbid:
        if i in s:
            return False


    numba = s[2:]
    isdig = False
    for i, ch in enumerate(numba):
        if ch.isdigit():
            if ch == '0' and not isdig:
                return False
            isdig = True
        elif ch.isalpha():
            if isdig:
                return False
        else:
            return False
    return True

main()
