

"""
Name: W. Aarts
Description: What's in your name? - a menu program that manipulates and
             interrogates a name. No string-class functions are used.
Bugs: None known
Bonus: title check, menu
Date: 9/30/2026
Log: 9/10/2026 Initial version
     9/30/2026 Added menu and all functions for the "what's in a name" project
     11/11/2026 Repairs: Added Docstrings for more heavy code, add descriptions for each
"""

import random


def main():
    """
    Des: Ask for your name, then let you pick things to do with it from a menu.
    Args: none.
    Returns: none.
    """
    while True:
        name = input("whats your name? : ")
        if not is_valid_name(name):
            print("letters only, no numbers or symbols")
        else:
            print(f"Thank you, {name}!")
            break
    """
    Des: Show the menu of options over and over until you pick 14 to quit.
    Args: none  uses the name you already typed in.
    Returns: none  just prints the menu.
    """
    while True:
        print(" 1. reverse")
        print(" 2. count vowels")
        print(" 3. count consonants")
        print(" 4. first name")
        print(" 5. last name")
        print(" 6. middle name")
        print(" 7. hyphen check (last name)")
        print(" 8. lowercase")
        print(" 9. uppercase")
        print(" 10. palindrome (first name)")
        print(" 11. mix up letters")
        print(" 12. initials")
        print(" 13. title check")
        print(" 14. quit")

        choice = input("choose a number: ")
        """
        Des: Run whatever option you picked on your name and print the answer.
        Args: choice (str)  the number you typed, name (str)  your name.
        Returns: none prints the result, or "not an option" if the number is wrong.
        """
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
            print(lower_caser(name))
        elif choice == "9":
            print(upper_caser(name))
        elif choice == "10":
            print(is_palindrome(name))
        elif choice == "11":
            print(random_name(name))
        elif choice == "12":
            print(initials(name))
        elif choice == "13":
            print(has_titles(name))
        elif choice == "14":
            print("goodbye!")
            break
        else:
            print("not an option try again")


def is_valid_name(name):
    """
    Des: Check that your name only uses letters, spaces, periods, or hyphens.
    Args: name (str)  the name you typed.
    Returns: bool  True if it's okay, False if it's empty or has numbers/symbols.
    """
    if name == "":
        return False
    for i in range(len(name)):
        if not (name[i].isalpha() or name[i] == " " or name[i] == "." or name[i] == "-"):
            return False
    return True


def reverse(name):
    """
    Des: Spell your name backwards.
    Args: name (str)  the name to flip.
    Returns: str  the name in reverse.
    """
    result = ""
    for i in range(len(name) - 1, -1, -1):
        result = result + name[i]
    return result


def vowel_counter(name):
    """
    Des: Count how many vowels are in your name.
    Args: name (str)  the name to count.
    Returns: int number of vowels.
    """
    count = 0
    for i in range(len(name)):
        if name[i] in "aeiouAEIOU":
            count = count + 1                          # count was set to zero, adds 1 to it if it detects one of the "aeiouAEIOU"
    return count


def consonant_counter(name):
    """
    Des: Count how many consonants are in your name.
    Args: name (str) the name to count.
    Returns: int number of consonants.
    """
    count = 0
    for i in range(len(name)):
        if name[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
            count = count + 1               #same here count is empty until you find a consonant, and adds it to the count
    return count


def split_name(name):
    """
    Des: Break your full name into separate words wherever there's a space.
    Args: name (str) the full name.
    Returns: list each word as its own string.
    """
    parts = []
    word = ""
    for i in range(len(name)):
        if name[i] == " ":                               # hit a space, so the current word is done
            parts = parts + [word]                       # add the finished word to the list
            word = ""                                    # reset word so the next one starts empty
        else:
            word = word + name[i]                        # not a space, so keep adding letters to the word
    parts = parts + [word]
    return parts


def first_name(name):
    """
    Des: Get your first name.
    Args: name (str) the full name.
    Returns: str the first word.
    """
    parts = split_name(name)
    return parts[0]


def last_name(name):
    """
    Des: Get your last name.
    Args: name (str)  the full name.
    Returns: str  the last word.
    """
    parts = split_name(name)                                                #uses my split name function
    return parts[len(parts) - 1]                                            # then steps back to last "part" and returns it


def middle_name(name):
    """
    Des: Get your middle name(s), if you have any.
    Args: name (str)  the full name.
    Returns: str  the middle name(s), or "" if there are none.
    """
    parts = split_name(name)
    result = ""
    for i in range(1, len(parts) - 1):
        result = result + parts[i] + " "
    return result


def hyphen_searcher(name):
    """
    Des: Check if your last name has a hyphen in it.
    Args: name (str) - the full name.
    Returns: bool - True if the last name is hyphenated.
    """
    last = last_name(name)
    for i in range(len(last)):   #goes to part of name last
        if last[i] == "-":       # then checks if it has hyphen in last name
            return True
    return False


def lower_caser(name):
    """
    Des: Turn your name into all lowercase letters.
    Args: name (str) - the name to change.
    Returns: str - the name in lowercase.
    """
    result = ""
    for i in range(len(name)):
        code = ord(name[i])
        if code >= 65 and code <= 90:              #ascii math, inside those numbers are capitals letterds represented as nubers
            result = result + chr(code + 32)       # detects those capital letters than returns them back as its lowercased number variant (+32)
        else:
            result = result + name[i]
    return result


def upper_caser(name):
    """
    Des: Turn your name into all uppercase letters.
    Args: name (str) - the name to change.
    Returns: str - the name in uppercase.
    """
    result = ""
    for i in range(len(name)):
        code = ord(name[i])
        if code >= 97 and code <= 122:             #these are lowercase numbers 97-122, detects them then returns back into uppercase lettrers
            result = result + chr(code - 32)       #automaticlaly filters out already uppercase letters
        else:
            result = result + name[i]
    return result


def random_name(name):
    """
    Des: Mix up the letters in your name into a random order.
    Args: name (str) - the name to scramble.
    Returns: str - the scrambled name.
    """
    letters = []
    for i in range(len(name)):
        letters = letters + [name[i]]                  # copy every letter of the name into a list
    result = ""
    while len(letters) > 0:
        j = random.randint(0, len(letters) - 1)        # pick a random spot in the list
        result = result + letters[j]                   # add that letter to the scrambled name
        letters = letters[0:j] + letters[j + 1:]       # remove it from the list so it isn't used twice
    return result


def is_palindrome(name):
    """
    Des: Check if your first name reads the same forwards and backwards.
    Args: name (str) - the full name.
    Returns: bool - True if the first name is a palindrome.
    """
    first = first_name(name)
    return first == reverse(first)


def initials(name):
    """
    Des: Get your initials.
    Args: name (str) - the full name.
    Returns: str - the first letter of each word.
    """
    parts = split_name(name)
    result = ""
    for i in range(len(parts)):
        result = result + parts[i][0]
    return result


def has_titles(name):
    """
    Des: Check if your name has a degree or title in it (like Ph.D. or III.).
    Args: name (str) - the full name.
    Returns: bool - True if a title is found.
    """
    titles = [
        "A.A.", "A.S.", "A.A.S.",
        "B.A.", "B.S.", "B.Sc.", "B.B.A.", "B.Ed.", "B.Eng.",
        "M.A.", "M.S.", "M.Sc.", "M.B.A.", "M.Ed.", "M.P.H.",
        "Ph.D.", "M.D.", "Ed.D.", "J.D.", "Pharm.D.",
        "I.", "II.", "III.", "IV.", "V."
    ]
    for i in range(len(titles)):
        if titles[i] in name:
            return True
    return False


main()