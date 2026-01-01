import os
import sys
from PIL import Image, ImageOps
count = len(sys.argv)
exten = ('.jpg'.casefold(),'.jpeg'.casefold(), '.png'.casefold())



if count < 3:
    print('Too few command-line arguments')
    sys.exit(1)
elif count > 3:
    print('Too many command-line arguments')
    sys.exit(1)

inin = sys.argv[1]
out = sys.argv[2]

extenin = os.path.splitext(inin)[1]
extenout = os.path.splitext(out)[1]

if not out.lower().endswith(exten):
    print('Invalid output')
    sys.exit(1)

if extenin != extenout:
    print('Input and output have different extensions')
    sys.exit(1)

if not os.path.exists(inin):
    print('Input does not exist')
    sys.exit(1)




shirt = Image.open('shirt.png')
person = Image.open(inin)
photo = ImageOps.fit(person, shirt.size)
photo.paste(shirt, shirt)
photo.save(out)
