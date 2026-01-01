d = input('How much was the meal? ')
p = input('What percentage would you like to tip ? ')

def main(dollar, percen):
    dollars = dollar
    percent = percen
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    nod = d.replace("$", "")
    nod = float(nod)
    return nod
def percent_to_float(p):
    nop = p.replace("%", "")
    nope = float(nop)
    noped = nope / 100
    return noped

yo = dollars_to_float(d)
yoo = percent_to_float(p)
main(yo,yoo)
