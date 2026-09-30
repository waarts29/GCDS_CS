# Wessel Aarts
# This code looksbat the mains and flairs and when you pick the amoun tof plates you want, it creates a randomized plate for each of the 5 and addds the main and flair price together, and creates a total price.
# 4/1/2026
# no bugs
# Generate and add in the costs for flairs as well. Calculate the total cost for all items. Ensure that the user is entering a valid number when asking for menu items. And make sure there will be no duplicate items.
# Google Slides


import random                         # enters randomization into the file

Mains = ["Cauliflower", "Tilapia_Filet", "Pork Loin", "Salmon", "Potatoes", "Three Color Squash", "Eggplant", "Steak", "Baguette"]      # lists all of the mains
Mains_Prices = [20, 25, 28, 30, 18, 20, 22, 30, 20]       # lists all the prices for mains

Flairs = ["with Balsamico", "with Garlic and Olive Oil", "with Minted Yogurt", "with Chutney", "Salad", "with Salsa", "over Sticky Rice", "Au Jus", "with Basmati Rice"] # lists all flairs
Flair_Prices = [7, 6, 8, 5, 4, 6, 4, 6, 6] # lists all flair prices

num_items = int(input("How many menu items do you need?\n>>> "))  # asks user for how many items they need through number

while num_items > len(Mains) or num_items <= 0:               # if number of items is more than the amount of mains
    print("please enter between 1 and", len(Mains), "items")  # makes it incorrect and asks for a number between on and 9
    num_items = int(input("How many menu items do you need?\n>>> "))  # asks the question again

total = 0   


main_indices = random.sample(range(len(Mains)), num_items)    # takes length of mains and generates a numebr of times the loop happens

for index in main_indices:       # for amount of mains asked and creates parallel array
    flair_index = random.randint(0, len(Flairs) - 1)  # finds length of flair options randomizes them and then chooses one

    main = Mains[index] # picks a food item from the main list in the current index
    main_price = Mains_Prices[index]  # picks a price that alligns with the main

    flair = Flairs[flair_index]   # picks a flair with the randomized index
    flair_price = Flair_Prices[flair_index]  # picks priuce that aligns with the flair

    item_total = main_price + flair_price  # adds up total price

    print(main + " " + flair + ", $" + str(item_total))    # prints total price
 
    total += item_total   # sets total cost.

print("Total price: $" + str(total)) # prints total price for user


