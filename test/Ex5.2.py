from pyfiglet import Figlet
import random
import emoji

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

figlet = Figlet()
x = list(figlet.getFonts())

figlet.setFont(font=x[random.randint(1,len(x))])

text = input(sys.argv)
for x in range(30):
    if x == 30:
        print(emoji.emojize(":beating_heart:"))
    else:
        print(emoji.emojize(":beating_heart:"), end="")
print("")
print(figlet.renderText(text))
for x in range(30):
    print(emoji.emojize(":beating_heart:"), end="")
    if x == 30:
        print(emoji.emojize(":beating_heart:"))



