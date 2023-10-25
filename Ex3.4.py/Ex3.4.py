def main():
    Plate = input("Plate: ")
    if isvalid(Plate) == True:
        print("Valid")
    else:
        print("Invalid")

def isvalid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        counter = 0
        new_counter = len(s)
        for char in s:
            counter += 1

            if char.isnumeric() == True and counter == 1:
                print("num1")
                return False
            if counter > 1 and char.isnumeric() == True:
                new_counter = counter
                if char == 0: 
                    print("numis0")                 
                    return False
                else:
                    print("done")
                    new_counter = counter
                    
                    
            
            if counter > new_counter and char.isalpha():
                print("wrong order")
                return False
            elif counter == len(s):
                print("Hi")
                return True
                    
                
        
    
main()
