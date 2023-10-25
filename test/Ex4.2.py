menu =  {
    "Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50,"Nachos": 11.00,
    "Quesadilla": 8.50,"Super Burrito": 8.50,"Super Quesadilla": 9.50,
    "Taco": 3.00,"Tortilla Salad": 8.00
    }

Summ = 0
while(True):
    order = input("Item: ").title()
    try:
        
        if order in menu:
            Summ += menu[order]
            print("Total: $",Summ, sep="")
        else:
            print("No")
        
    except EOFError:
        print("Hu")
        break


    