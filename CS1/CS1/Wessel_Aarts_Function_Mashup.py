import random 


def chorus(name, age):
    '''''
    Prints the first three lines of the Happy Birthday song.

    Args:
        name (str): he name of the person being sung to.
        age (str): The age of the person (unused in output but kept for signature consistency).
    Return/Print:
        Print thre lines of the Happy Birthday song to the console.
    '''
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}")


def sing_song():
    '''
    Prompts the user for their name and age, then sings the full Happy Birthday song.

    Args:
        None
    Return/Print:
        Prints the full Happy Birthday song including the age counting line to the console.
    '''
    name = input("Enter your name: ")
    age = input("How old are you? ")
    chorus(name, age)
    print(f"Happy birthday, {name}")
    print("Happy birthday to you")
    print("Are you one, are you two, are you three, are you four, are you five... I am " + age)


def add(number_1, number_2):
    '''
    Adds two numbers together and returns the result.

    Args:
        number_1 (int | float): The first number.
        number_2 (int | float): The second number.
    Return/Print:
        result (int | float): The sum of number_1 and number_2.
    '''
    return number_1 + number_2


def print_list(my_list):
    '''
    Prints each element of a list on a separate line.

    Args:
        my_list (list): The list of items to print.
    Return/Print:
        Prints each item in my_list to the console on its own line.
    '''
    for item in my_list:
        print(item)


def in_list(my_list, element):
    '''
    Checks whether a given element exists in a list.

    Args:
        my_list (list): The list to search through.
        element (any): The element to look for in the list.
    Return/Print:
        found (bool): True if element is in my_list, False otherwise.
    '''
    return element in my_list


def is_integer(value):
    '''
    Determines whether a given value can be converted to an integer.

    Args:
        value (any): The value to check.
    Return/Print:
        result (bool): True if value is convertible to an integer, False otherwise.
    '''
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False


def get_integer():
    '''
    Prompts the user to enter a valid integer, retrying recursively if input is invalid.

    Args:
        None
    Return/Print:
        value (int): A valid integer entered by the user.
    Raises:
        RecursionError: If the user repeatedly enters invalid input exceeding Python's recursion limit.
    '''
    value = input("Enter a number: ")
    if is_integer(value):
        return int(value)
    else:
        print("That is not a valid integer, try again!")
        return get_integer()


def get_random():
    '''
    Prompts the user for a lower and upper bound, then prints a random integer in that range.

    Args:
        None
    Return/Print:
        Prints a random integer between lower and upper (inclusive) to the console.
    '''
    print("Enter a lower number:")
    lower = get_integer()
    print("Enter a higher number:")
    upper = get_integer()
    print(random.randint(lower, upper))


def count_vowels(string):
    '''
    Counts the total number of vowels in a string and prints a breakdown by vowel.

    Args:
        string (str): The input string to analyze.
    Return/Print:
        Prints a subtotal count per vowel and the overall total to the console.
        total (int): The total number of vowels found in the string.
    '''
    vowels = "aeiouAEIOU"
    subtotals = {v.lower(): 0 for v in "aeiou"}

    for char in string:
        if char in vowels:
            subtotals[char.lower()] += 1

    total = sum(subtotals.values())
    print(f"Subtotals: {subtotals}")
    print(f"Total vowels: {total}")
    return total


def reverse_string(string):
    '''
    Reverses a given string and prints the result.

    Args:
        string (str): The input string to reverse.
    Return/Print:
        Prints the reversed string to the console.
        reversed_str (str): The reversed version of the input string.
    '''
    reversed_str = string[::-1]
    print("Reversed string:", reversed_str)
    return reversed_str


def main():
    print(" Birthday Song ")
    sing_song()

    print(" Addition ")
    number_1 = int(input("Pick a random number: "))
    number_2 = int(input("Pick a random number: "))
    result = add(number_1, number_2)
    print("Your total is:", result)

    print(" Fruit List ")
    fruits = ["apple", "banana", "cherry", "mango", "orange"]
    print_list(fruits)
    print(in_list(fruits, "banana"))
    print(in_list(fruits, "mango"))
    print(in_list(fruits, "grape"))

    print(" Integer Validator ")
    result = get_integer()
    print("You entered:", result)

    print("Random Number Generator ")
    get_random()

    print(" Vowel Counter ")
    user_string = input("Enter a string to count vowels: ")
    count_vowels(user_string)

    print(" String Reverser ")
    user_string = input("Enter a string to reverse: ")
    reverse_string(user_string)


if __name__ == "__main__":
    main()