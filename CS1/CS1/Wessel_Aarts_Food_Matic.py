# Wessel Aarts
# This code looksbat the mains and flairs and when you pick the amoun tof plates you want, it creates a randomized plate for each of the 5 and addds the main and flair price together, and creates a total price.
# 4/1/2026
# no bugs
# Generate and add in the costs for flairs as well. Calculate the total cost for all items. Ensure that the user is entering a valid number when asking for menu items. And make sure there will be no duplicate items.
# Google Slides


import random 

Mains = ["Cauliflower", "Tilapia_Filet", "Pork Loin", "Salmon", "Potatoes", "Three Color Squash", "Eggplant", "Steak", "Baguette"]
Mains_Prices = [20, 25, 28, 30, 18, 20, 22, 30, 20]

Flairs = ["with Balsamico", "with Garlic and Olive Oil", "with Minted Yogurt", "with Chutney", "Salad", "with Salsa", "over Sticky Rice", "Au Jus", "with Basmati Rice"]
Flair_Prices = [7, 6, 8, 5, 4, 6, 4, 6, 6]

num_items = int(input("How many menu items do you need?\n>>> ")) 

while num_items > len(Mains) or num_items <= 0:
    print("please enter between 1 and", len(Mains), "items")
    num_items = int(input("How many menu items do you need?\n>>> "))

total = 0  


main_indices = random.sample(range(len(Mains)), num_items)

for index in main_indices:
    flair_index = random.randint(0, len(Flairs) - 1)

    main = Mains[index]
    main_price = Mains_Prices[index]

    flair = Flairs[flair_index]
    flair_price = Flair_Prices[flair_index]

    item_total = main_price + flair_price

    print(main + " " + flair + ", $" + str(item_total))

    total += item_total

print("Total price: $" + str(total))


