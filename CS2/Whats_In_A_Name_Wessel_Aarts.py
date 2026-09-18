#rellok at firts and last names
#for uppercase do like letter = ord(letter) then if letter >=65 and <= 92 its uppercaseothe way for lowers etc




def main():
    name = input("whats your name? : ")
    while True:
        print(" 1. reverse")
        print(" 2. count vowels")
        print(" 3. count consonants")
        print(" 4. first name")
        print(" 5. last name")
        print(" 6. quit")
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


def first_name(name):
    result = ""
    for i in range(len(name)):
        if name[i] == " ":     
            break
        result = result + name[i]
    return result


def last_name(name):
    result = ""
    for i in range(len(name)):
        if name[i] == " ":      
            result = ""         
        else:
            result = result + name[i]
    return result


main()