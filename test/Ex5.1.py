import emoji
# emojiis = input("..")
# print(emoji.emojize("Emoji ", emojiis, language="alias"))
# print(emoji.emojize("Emoji :thumbsup:", emojiis, language="alias"))
#print(emoji.emojize("Python is :thumbs_up:"))
a,b,c = input("Input:").strip(" ").split(":")
b = ":"+b+":"

for letter in b:
    if letter == "_":
        print(emoji.emojize("{0}{1}{2}".format(a,b,c)),sep="")
        break
    else:
        print(emoji.emojize("{0}{1}{2}".format(a,b,c),language="alias"),sep="")
        break

