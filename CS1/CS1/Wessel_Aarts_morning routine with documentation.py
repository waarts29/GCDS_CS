print('Alarm!!!')                                                                  #terminal says Alarm!!
print("dont forget to make your bed!!")                                            # terminal says dont forget to make your bed!!

while True:                                                                        # forever loop
    snooze_for_five_minutes = input('Snooze for five minutes? yes/no: ')           #asks the user if it wants to snooze or not
    if snooze_for_five_minutes == "yes":                                           # does the user want to snooze for five minutes
        print('go back to sleep')                                                  # if yes then user sees go back to sleep
    elif snooze_for_five_minutes == "no":                                          # if the user does not agree with the if statement they go to elif statement that they dont want to snooze for five minutes
        print('wake up')                                                           # then it says wake up
        break                                                                      # stops the loop

print("welcome to your water reminder!")                                           # says welcome to your water reminder in terminal
import time                                                                        #  brings time into code
minutes = int(input("remind after how many minutes, type 0 if testing"))           # type in an intrger the goes into terminal and asks how many mintes the user wants to be reminded
seconds = minutes * 60                                                             # setting 1 minute to 60 seconds bc thats how th code works
 
print("ok, ill remind you in {minutes} ")                                          # it will remind the user in the terminal in however many minutes they put in the terminal

while seconds > 0:                                                                 # forvevry loop that makes sure the loop of time keeps going until the amount of seconds is less than 0 so when the time runs out 
     print("{seconds} seconds left")                                               # this prints every seconds how many time is left before the reminder ends 
     time.sleep(1)                                                                 # means that the program will be stopped for 1 second
     seconds -= 1                                                                  # tells to decrement the code by one second every second to make sure the timer keeps going
print ("drink water!!")                                                            # if the loop is finished it prints in temrninal drink water

while True:                                                                        # forever loop
    temperature = int(input("what is the temperature in farenheight "))            # you ask the user what the temp is outside 
    if temperature <= 50:                                                          # if the temperature is lower than 50 it does something
        print('bring a coat')                                                      # it says bring a coat if the if statement is true
    elif temperature >50:                                                          # otherwise if the temp is greater than 50 then you bring a tshirgt
        print("bring a t shirt")                                                   # then if the elif statement is true it print sin terminal bring a t shirt
    break                                                                          # stops loop then brings to next while true loop

while True:                                                                        # forever loop
    rainy = input('rainy? yes/no:')                                                # asks the user if it is rainy outside
    if rainy == "yes":                                                             # if its rainy then type yes
        print ("put jacket in backpack")                                           # then print put jacket in backpack if the use rtyped yes
    elif rainy == "no":                                                            # otherwise if its not rainy
        print ("dont get jacket")                                                  # then dont bring jacket
    break                                                                          # then stop code

print("welcome to your daily, go outside after waking up reminder!!!!")            # pritns int erminal wlecome to daily water eminder
import time                                                                        # brings time into the terminal
minutes = int(input("remind after how many minutes, type 0 if testing"))           # asks user in integers after how many minutes they want their reminder
seconds = minutes * 60                                                             # setting time to 60 seconds not 1 minute
 
print("ok, ill remind you in {minutes} ")                                          # once user statement is put in the terminal starts the seconds 

while seconds > 0:                                                                 # stops when the time is less than 0
     print("{seconds} seconds left")                                               #  then it prints hpow many secodns is left
     time.sleep(1)                                                                 # means program will be stopped ofr 1 second
     seconds -= 1                                                                  # tells code to decrement evry one secodns so time rowrks
print ("get fresh air!!")                                                          # once loopp is over the terminal prints get fresh air

while True:                                                                        # forever loop
    showered_last_night = input('shower_last_night? yes/no:')                      # asks the user if they showered last night
    if showered_last_night == "yes":                                               #  if the user says yes to showering then
        print ("dont shower")                                                      # it prints dont shower
    elif showered_last_night == "no":                                              # otherwise if the user types in no
        print ("shower for 10 mins")                                               # then the terminal syas shower for ten minutes
    else:                                                                          # else 
        print ("please answer")                                                    # to make sure the user answers 
    break                                                                          # ends loop when they either said yes or no

while True:                                                                        # forever loop
    Homework = input('homework yes/no:')                                           # asks thew user if they did hoemwork
    if Homework == "yes":                                                          # if user says yes then 
        print ("stay home for 20min extra")                                        # they can stay hoem for more time which syas in the terminal
    elif Homework == "no":                                                         # otherwise if the user says no 
        print ("go to school early")                                               # then it pritns go to school early
    else:                                                                          # else
        print ("please answer yes/no")                                             # if user doesnt type yes or no this makes rue they do
    break                                                                          # stops the code afetr answering yes or no

while True:                                                                        # forever loop
    have_time_for_breakfast = input('have_time_for_breakfast ')                    # then asks the user if they have time for user
    if have_time_for_breakfast == "yes":                                           # if the user says yes then
        print ("eat with friends")                                                 # it prints eat with friends
    elif have_time_for_breakfast == input('have_time_for_breakfast'):              # otherwise they have dont time for breakfast
        print ("grab a bagel")                                                     # grab a bagel in terminal
        print ("go to homeroom")                                                   # go to homework in terminal
    break                                                                          # stops loop afetr yes or no 

while True:                                                                        # forver loop
    what_class_do_I_have = input("what_class_do_I_have")                           # asks the user what classs they have
    if what_class_do_I_have == "math":                                             # if classs is math the n
            print ("bring Calculator")                                             # says in terminal bring a claculator
    elif what_class_do_I_have == "english":                                        # if its english then
            print ("bring Animal Farm Book")                                       # bring animal farm book 
    elif what_class_do_I_have == "comp sci":                                       # asks user what class they have if they answer comp sci 
            print (" bring computer")                                              # it says in terminal bring computer 
    elif what_class_do_I_have == "seminar":                                        # if the class user has is seminar then
            print ("bring notebook")                                               # bring notebook
    elif what_class_do_I_have == "social studies":                                 # asks user if they have social studies
            print ("bring notebook")                                               # then it says to user bring notebook
    break                                                                          # stops loop after user answers a correct answer
    



