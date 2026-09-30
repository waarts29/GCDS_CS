def chorus(name, age):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}")  

def sing_song():
    name = input("enter your name")
    age = input(" how old are you")
    chorus(name, age)
    print(f" Happy birthday, " + name)  
    print(" Happy birthday to you")
    print(" are you one, are you two, are you three, are you four, are you five... I am " + age)

sing_song()

number_1 = int(input("Pick a random number: "))
number_2 = int(input("Pick a random number: "))

print("next mashup")

def add(number_1, number_2):
    z = number_1 + number_2
    return z

result = add(number_1, number_2)
print("Your total is:", result)

print("next mashup")

def print_list(my_list):
    for item in my_list:
        print(item)

def in_list(my_list, element):
    return element in my_list

fruits = ["apple", "banana", "cherry", "mango", "orange"]

print_list(fruits)

print(in_list(fruits, "banana"))
print(in_list(fruits, "mango"))
print(in_list(fruits, "grape"))

print("next mashup")


def is_integer(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False

def get_integer():
    value = input("Enter a number: ")
    if is_integer(value):
        return int(value)
    else:
        print("That is not a valid integer, try again!")
        return get_integer()

result = get_integer()
print("You entered:", result)


import random

def get_random():
    print("lower number")
    lower = get_integer()
    print("enter a higher number")
    upper = get_integer()
    print(random.randint(lower, upper))

get_random()


def count_vowels(string):
    vowels = "aeiouAEIOU"
    subtotals = {v.lower(): 0 for v in "aeiou"}
    
    for char in string:
        if char in vowels:
            subtotals[char.lower()] += 1
    
    total = sum(subtotals.values())
    
    print(f"Subtotals: {subtotals}")
    print(f"Total vowels: {total}")
    
    return total  