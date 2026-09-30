def get_number():
    while True:
        try:
            num = int(input("enter a number:"))
        except ValueError:
            print(" please enter a integer")
            continue
        if num > 0:
         return num 
        
def add_number():
    num1 = get_number()
    num2 = get_number()
    
    return num1 + num2

def main():
   res1 = add_number()
   res2 = add_number()

   print(res1, res2)

main()
