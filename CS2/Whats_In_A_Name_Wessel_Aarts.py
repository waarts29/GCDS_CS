#rellok at firts and last names
#for uppercase do like letter = ord(letter) then if letter >=65 and <= 92 its uppercaseothe way for lowers etc
import random 



def main():
    while True:
        name = input("whats your name? : ")
        valid = True
        for i in range(len(name)):
            if not (name[i].isalpha() or name[i] == " "):
                valid = False
        if name == "" or valid == False:
            print("letters only, no numbers or symbols")
        else:
            print(f"Thank you, {name}!")
            break
            
    
    while True:
        print(" 1. reverse")
        print(" 2. count vowels")
        print(" 3. count consonants")
        print(" 4. first name")
        print(" 5. last name")
        print(" 6. middle name")
        print(" 7. hyphen check")
        print(" 8. lowercase")
        print(" 9. uppercase")
        print(" 10. palindrome ")
        print(" 11. quit")
        
        choice = input("choose a number: ")
        
        if choice == "1":
            print(reverse(name))
        elif choice == "2":
            print(vowel_counter(name))
        elif choice == "3":
            print(consonant_counter(name))
        elif choice == "4":
            print(first_name(name))
        elif choice == "5":
            print(last_name(name))
        elif choice == "6":
            print(middle_name(name))
        elif choice == "7":
            print(hyphen_searcher(name))
        elif choice == "8":
            print(lowercasermaker(name))
        elif choice == "9":
            print(uppercasermaker(name))
        elif choice == "10":
            print(is_palindrome(name))
        elif choice == "11":
            print("goodbye!")
            break  
        else:
            print("not an option try again")



def reverse(name):
    result = ""
    for i in range(len(name) - 1, -1, -1):
        result = result + name[i]
    return result


def vowel_counter(name):
    count = 0
    for i in range(len(name)):
        if name[i] in "aeiouAEIOU":
            count = count + 1
    return count


def consonant_counter(name):
    count = 0
    for i in range(len(name)):
        if name[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
            count = count + 1
    return count

    


def split_name(name):
    parts = []
    word = ""
    for i in range(len(name)):
        if name[i] == " ":
            parts = parts + [word]
            word = ""
        else:
            word = word + name[i]
    parts = parts + [word]
    return parts


def first_name(name):
    parts = split_name(name)
    return parts[0]


def last_name(name):
    parts = split_name(name)
    return parts[len(parts) - 1]


def middle_name(name):
    parts = split_name(name)
    result = ""
    for i in range(1, len(parts) - 1):
        result = result + parts[i] + " "
    return result

def hyphen_searcher(name):
    for i in range(len(name)):
        if name[i] == "-":
            return True
    return False

def lowercasermaker(name):
    result = ""
    for i in range(len(name)):
        code = ord(name[i])
        if code >= 65 and code <= 92:
            result = result + chr(code + 32)
        else:
            result = result + name[i]
    return result

def uppercasermaker(name):
    result = ""
    for i in range(len(name)):
        code = ord(name[i])
        if code >=97 and code <= 122:
            result = result + chr(code -32)
        else:
            result = result +name[i]
    return result

#do random name here

def is_palindrome(name):
    return name == reverse(name)  



      


    




main()