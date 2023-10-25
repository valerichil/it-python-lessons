import random


def main():
    x = get_level()
    generate_integer(x)


def get_level():
    while(True):
        try:
            Choose_level = int(input("Level: "))
            levels = [1,2,3]
            if Choose_level in levels:
                return Choose_level
            else: 
                continue
        except ValueError:
            continue



def generate_integer(level):
    n = 0
    for problem in range(10):
        x = random.randint(1,2*level)
        y = random.randint(1,3*level)
        
        while(True):
            try:
                
                print(str(x) +" + "+ str(y) + " = ", end="")
                User_answer = int(input(""))
                
                if User_answer == (x + y):
                    n += 1
                    break
                else:
                    print("EEE")
                    for falseanswer in range(2):
                        print(str(x) +" + "+ str(y) + " = ", end="")
                        User_answer = int(input(""))
                        if User_answer is not (x + y):
                            print("EEE")
                            continue
                        else:
                            break
                    else:
                        print(str(x) +" + "+ str(y) + " = " + str(x+y))
                        break
                    break
                        
                        
                    
                
            except ValueError:
                continue
    print("Your score is:", n)



if __name__ == "__main__":
    main()
