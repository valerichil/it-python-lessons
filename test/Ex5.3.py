#try:
names = []
while(True):
    name = input("Name: ")
    names.append(name)
        
    if name == "END":
        count = len(names)
        print("Adieu, adieu, to ",end="")
        for name in names:
            if count == 2:
                print(name)
                break
            elif name == names[-2] and count > 2:
                print("and "+name)
                break
            else:
                print(name+",",end=" ")
        break
    else:
        continue