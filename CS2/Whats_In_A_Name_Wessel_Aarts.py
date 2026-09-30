import random


def main():
    """Validate the name, then loop a menu of options until the user quits.
    Args: none.
    Returns: none.
    """
    while True:
        name = input("whats your name? : ")
        valid = True
        for i in range(len(name)):
            if not (name[i].isalpha() or name[i] == " " or name[i] == "." or name[i] == "-"):
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
        print(" 7. hyphen check (last name)")
        print(" 8. lowercase")
        print(" 9. uppercase")
        print(" 10. palindrome (first name)")
        print(" 11. mix up letters")
        print(" 12. initials")
        print(" 13. title check")
        print(" 14. quit")

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


def reverse(name):
    """Return the string with its characters in reverse order.
    Args: name (str) - word or name to reverse.
    Returns: str.
    """
    result = ""
    for i in range(len(name) - 1, -1, -1):
        result = result + name[i]
    return result


def vowel_counter(name):
    """Count the vowels in a string     (upper and lower case).
    Args: name (str)  word or name to search.
    Returns: int  number of vowels.
    """
    count = 0
    for i in range(len(name)):
        if name[i] in "aeiouAEIOU":
            count = count + 1
    return count


def consonant_counter(name):
    """Count the consonants in a string (upper and lower case).
    Args: name (str) - word or name to search.
    Returns: int - number of consonants.
    """
    count = 0
    for i in range(len(name)):
        if name[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
            count = count + 1
    return count


def split_name(name):
    """Break a full name into a list of its words (hand-built, no .split()).
    Builds one word at a time; each space ends a word and starts the next.
    Args: name (str) - the full name.
    Returns: list - the words as separate strings.
    """
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
    """Return the first word of a full name.
    Args: name (str) - the full name.
    Returns: str.
    """
    parts = split_name(name)
    return parts[0]


def last_name(name):
    """Return the last word of a full name.
    Args: name (str) - the full name.
    Returns: str.
    """
    parts = split_name(name)
    return parts[len(parts) - 1]


def middle_name(name):
    """Return the middle name(s), or "" if there are none.
    Args: name (str) - the full name.
    Returns: str.
    """
    parts = split_name(name)
    result = ""
    for i in range(1, len(parts) - 1):
        result = result + parts[i] + " "
    return result


def hyphen_searcher(name):
    """Return True if the last name contains a hyphen.
    Args: name (str) - the full name.
    Returns: bool.
    """
    last = last_name(name)
    for i in range(len(last)):
        if last[i] == "-":
            return True
    return False


def lowercasermaker(name):
    """Convert a string to lowercase using ASCII.
    Uppercase codes are 65-90, adding 32 gives the lowercase letter.
    Args: name (str) - the string to convert.
    Returns: str.
    """
    result = ""
    for i in range(len(name)):
        code = ord(name[i])
        if code >= 65 and code <= 90:
            result = result + chr(code + 32)
        else:
            result = result + name[i]
    return result


def uppercasermaker(name):
    """Convert a string to uppercase using ASCII math .
    Lowercase codes are 97-122; subtracting 32 gives the uppercase letter.
    Args: name (str) the string to convert.
    Returns: str.
    """
    result = ""
    for i in range(len(name)):
        code = ord(name[i])
        if code >= 97 and code <= 122:
            result = result + chr(code - 32)
        else:
            result = result + name[i]
    return result


def random_name(name):
    """Scramble a name's letters into a random order.
    Copies letters to a list, then pulls out a random one at a time.
    Args: name (str), the name to scramble.
    Returns: str.
    """
    letters = []
    for i in range(len(name)):
        letters = letters + [name[i]]
    result = ""
    while len(letters) > 0:
        j = random.randint(0, len(letters) - 1)
        result = result + letters[j]
        letters = letters[0:j] + letters[j + 1:]
    return result


def is_palindrome(name):
    """Return True if the first name reads the same forwards and backwards.
    Args: name (str),  the full name.
    Returns: boolean.
    """
    first = first_name(name)
    return first == reverse(first)


def initials(name):
    """Return the first letter of every word in the name.
    Args: name (str),  the full name.
    Returns: str.
    """
    parts = split_name(name)
    result = ""
    for i in range(len(parts)):
        result = result + parts[i][0]
    return result


def has_titles(name):
    """Return True if the name contains a title or distinction.
    Args: name (str),  the name to check.
    Returns: boolean.
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
