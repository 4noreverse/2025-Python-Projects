from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
argcount = len(sys.argv)


if argcount != 1 and argcount != 3:
    sys.exit(1)


if argcount == 1:
    f = figlet.getFonts()
    new = random.choice(f)
    figlet.setFont(font=new)
    mess = input('Input: ')
    print(figlet.renderText(mess))


elif argcount == 3:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit(1)


    sont = sys.argv[2]
    allfont = figlet.getFonts()


    if sont not in allfont:
        sys.exit(1)


    s = figlet.getFonts()
    figlet.setFont(font=sont)
    mess = input('Input: ')
    print(figlet.renderText(mess))





