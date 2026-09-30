print('Alarm!!!')
print("dont forget to make your bed!!")

while True:
    snooze_for_five_minutes = input('Snooze for five minutes? yes/no: ')
    if snooze_for_five_minutes == "yes":
        print('go back to sleep')
    elif snooze_for_five_minutes == "no":
        print('wake up')
        break

print("welcome to your water reminder!") 
import time
minutes = int(input("remind after how many minutes, type 0 if testing")) 
seconds = minutes * 60

print("ok, ill remind you in {minutes} ")

while seconds > 0:
     print("{seconds} seconds left")
     time.sleep(1)
     seconds -= 1
print ("drink water!!")

while True:
    temperature = int(input("what is the temperature in farenheight "))
    if temperature <= 50:
        print('bring a coat')
    elif temperature >50:
        print("bring a t shirt")
    break

while True:
    rainy = input('rainy? yes/no:')
    if rainy == "yes":
        print ("put jacket in backpack")
    elif rainy == "no":
        print ("dont get jacket")
    break  

print("welcome to your daily, go outside after waking up reminder!!!!") 
import time
minutes = int(input("remind after how many minutes, type 0 if testing")) 
seconds = minutes * 60

print("ok, ill remind you in {minutes} ")

while seconds > 0:
     print("{seconds} seconds left")
     time.sleep(1)
     seconds -= 1
print ("get fresh air!!")

while True:
    showered_last_night = input('shower_last_night? yes/no:')
    if showered_last_night == "yes":
        print ("dont shower")
    elif showered_last_night == "no": 
        print ("shower for 10 mins")
    else:
        print ("please answer")
    break

while True:
    Homework = input('homework yes/no:')
    if Homework == "yes":
        print ("stay home for 20min extra")
    elif Homework == "no":
        print ("go to school early")
    else:
        print ("please answer yes/no")
    break

while True:
    have_time_for_breakfast = input('have_time_for_breakfast ')
    if have_time_for_breakfast == "yes":
        print ("eat with friends")
    elif have_time_for_breakfast == input('have_time_for_breakfast'):
        print ("grab a bagel")
        print ("go to homeroom")
    break

while True:
    what_class_do_I_have = input("what_class_do_I_have")  
    if what_class_do_I_have == "math":
            print ("bring Calculator")
    elif what_class_do_I_have == "english":
            print ("bring Animal Farm Book")
    elif what_class_do_I_have == "comp sci":
            print (" bring computer")
    elif what_class_do_I_have == "seminar":
            print ("bring notebook")
    elif what_class_do_I_have == "social studies":
            print ("bring notebook")
    break
    



