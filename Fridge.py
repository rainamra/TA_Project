miniFridge_items: {str: int} = {}

open_miniFridge = True

def put_items(put_skincare, number_of_items):
    if put_skincare in miniFridge_items:
        miniFridge_items[put_skincare] += number_of_items
    else:
        miniFridge_items[put_skincare] = number_of_items

def take_items(take_skincare, left_items):
    if question1_2_1 > miniFridge_items[question1_2]:
        print("There is not enough " + question1_2 + " to take out.")
        print("You only have: " + miniFridge_items[question1_2])
    elif question1_2_1 <= miniFridge_items[question1_2]:
        print("Enjoy the " + question1_2)
    elif take_skincare in miniFridge_items:
        miniFridge_items[take_skincare] -= left_items
    else:
        print("There is no", take_skincare, "in fridge !")

def view_items():
    if miniFridge_items.items() != 0:
        for i in miniFridge_items.items():
            print(i)
            print("==========================")


while True:
    while open_miniFridge:

        print("\nSkincare Mini Fridge")
        print("------------------------")
        user = input("What is your name?")
        print("Hey,",user.title(),"!")
        question = input("Would you like to open the Mini Fridge? Y/N")
        if question.lower() == "y":
            print("Okey",user.title(),"!")
            question1 = input("Choose an action: put/view/take")
            if question1.lower() == "put":
                question1_1 = input("What skincare would you like to put?")
                question1_1_1 = input("How many " + question1_1 + " would you like to put?")
                put_items(question1_1, question1_1_1)
                print(question1_1, "is now in the mini fridge")
            elif question1.lower() == "view":
                print("==========================")
                print(view_items())
                print("==========================")
            elif question1.lower() == "take":
                question1_2 = input("What skincare would you like to take out?")
                question1_2_1 = input("How many " + question1_2 + " would you like to take out?")
                take_items(question1_2, question1_2_1)
                print("Don't forget to do your skincare routine :)")
            else:
                print("Your input is invalid")
        elif question.lower() == "n":
            print("Okey! bye", user.title())
        else:
            print("Your input is invalid.")










