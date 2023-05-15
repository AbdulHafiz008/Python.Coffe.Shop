import time
import random

print("Hello, welcome to the Python Coffee Shop!")
time.sleep(random.uniform(0.2, 0.4))

name = input("What is your name?")
time.sleep(random.uniform(0.2, 0.4))

if name.lower() == "Bjørn":
    bjørn_status = int(input("What grade will I get for this?"))
    time.sleep(random.uniform(0.2, 0.4))

    if bjørn_status == 6:
        print("Well, you are welcome.")
        time.sleep(random.uniform(0.2, 0.4))
    elif bjørn_status == 5:
        print("Why the F@#K would I get a 5?")
        time.sleep(random.uniform(0.2, 0.4))
        print("Sorry, you are kicked out of this coffee shop!")
        exit()
    elif bjørn_status in [4, 3, 2, 1]:
        print("Well, that is very racist.")
        time.sleep(random.uniform(0.2, 0.4))
        print("Man, get your a#s out of here.")
        exit()

time.sleep(random.uniform(0.2, 0.4))
print(name.capitalize() + ", what would you like?")
time.sleep(random.uniform(0.2, 0.4))
print(name.capitalize() + ", we have:")

menu_items = ["Coffee", "Tea", "Sandwiches", "Pastries", "Salads", "Smoothies", "Soup", "Burgers", "Wraps", "Milkshakes"]

for item in menu_items:
    time.sleep(0.1)
    print("- " + item)
