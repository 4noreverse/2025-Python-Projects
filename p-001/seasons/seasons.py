import datetime
import sys
import math
from datetime import date
from datetime import time
import inflect

def main():
    try:
        year, month, day = map(int, input('Date of Birth: ').split('-'))
        dob = date(year, month, day)
    except ValueError:
        sys.exit(1)

    print(f'{jork(dob)} minutes')



def jork(dob):
    p = inflect.engine()
    today = date.today()
    delt = today - dob
    answer = delt.total_seconds() // 60
    final = p.number_to_words(int(answer), andword="").capitalize()
    return final



if __name__ == "__main__":
    main()
