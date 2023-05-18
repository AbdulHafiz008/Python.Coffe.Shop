import random
import time

print("Hello, welcome to the Python Coffee Shop!")
time.sleep(random.uniform(0.2, 0.4))

name = input("What is your name?")
time.sleep(random.uniform(0.2, 0.4))

if name.lower() == "bjørn":
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

while True:
    for item in menu_items:
        time.sleep(0.1)
        print("- " + item)

    order = input("What do you want?")

    if order.lower() in menu_items:
        print(name.capitalize() + ", your order will be ready soon.")
        break
    else:
        print("Sorry, we don't have that available in our shop!")
        time.sleep(0.3)
        print("Please choose something from the menu.")
        time.sleep(random.uniform(0.2, 0.4))

while True:
    try:
        amount = int(input(name.capitalize() + ", how many " + order.lower() + " do you want?"))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

price = 9
total = price * amount

print(name.capitalize() + ", just wait a second and your " + order.lower() + " will be ready.")

for i in range(10, 0, -1):
    print("Kø", i)
    time.sleep(0.5)

print("Your order of " + str(amount) + " " + order.lower() + " is ready now.")
time.sleep(0.3)

while True:
    pay_type = input("How would you like to pay?\nCard or Cash")
    if pay_type.lower() in ["card", "cash"]:
        print("You can now pay and get your order.")
        break
    else:
        print("Sorry, we don't have that payment type!")

print("Here is your order.")

while True:
    rate = input("What will you rate our shop out of 6?")
    if int(rate) > 5:
        print("Thanks for your kind response and rating!")
        break
    else:
        improvement = input("What can we do better?")
        print("Thank you for your feedback. We will work on improving.")
        break
