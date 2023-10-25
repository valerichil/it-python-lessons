grocery_list = {}

while(True):
    add_item = input("").upper
    try:
        if add_item in grocery_list:
            grocery_list[add_item] += 1
        else:
            grocery_list[add_item] = 1
    # except EOFError:
    #     for item in grocery_list:
    #         print(grocery_list[item], item)
    #         break
    except KeyError:
        print("wrong key")
    if add_item == "gg":
        for item in grocery_list:
            print(grocery_list[item], item)
        break