print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

Bill = 0

# S = 15
# M = 20
# L = 25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

if size == "S":
    Bill = 15
    add_pepperoni
    if add_pepperoni == "Y":
        Bill += 2
        extra_cheese
        if extra_cheese == "Y":
            Bill += 1
            print(f"Your final bill is: ${Bill}.")
        elif extra_cheese == "N":
            print(f"Your final bill is: ${Bill}.")
    elif add_pepperoni == "N":
        extra_cheese
        if extra_cheese == "Y":
            Bill += 1
            print(f"Your final bill is: ${Bill}.")
        elif extra_cheese == "N":
            print(f"Your final bill is: ${Bill}.")
    else:
        print(f"Your final bill is: ${Bill}.")
elif size == "M":
    Bill = 20
    add_pepperoni
    if add_pepperoni == "Y":
        Bill += 3
        extra_cheese
        if extra_cheese == "Y":
            Bill += 1
            print(f"Your final bill is: ${Bill}.")
        elif extra_cheese == "N":
            print(f"Your final bill is: ${Bill}.")
    elif add_pepperoni == "N":
        extra_cheese
        if extra_cheese == "Y":
            Bill += 1
            print(f"Your final bill is: ${Bill}.")
        elif extra_cheese == "N":
            print(f"Your final bill is: ${Bill}.")
    else:
        print(f"Your final bill is: ${Bill}.")
elif size == "L":
    Bill = 25
    add_pepperoni
    if add_pepperoni == "Y":
        Bill += 3
        extra_cheese
        if extra_cheese == "Y":
            Bill += 1
            print(f"Your final bill is: ${Bill}.")
        elif extra_cheese == "N":
            print(f"Your final bill is: ${Bill}.")
    elif add_pepperoni == "N":
        extra_cheese
        if extra_cheese == "Y":
            Bill += 1
            print(f"Your final bill is: ${Bill}.")
        elif extra_cheese == "N":
            print(f"Your final bill is: ${Bill}.")
    else:
        print(f"Your final bill is: ${Bill}.")
