items = [
    (" Balde        ", 1, 10),
    (" Chicken Joy  ", 2, 15),
    (" Hollow Blocks", 3, 40),
]

MAX_WEIGHT = 5


def show_items():
    print("\nAvailable Items in House:")
    print("Items | Type of Items | Weight | Value")
    for i, t in enumerate(items, start=1):
        print(f"  {i}   |{t[0]:15}|{t[1]:4}    |  ₱{t[2]}")


def manual_selection():
    chosen = []
    total_weight = 0
    total_value = 0

    while True:
        print("")
        show_items()
        print(f"\nWeight In Bag (kg): {total_weight}/{MAX_WEIGHT}")
        print("What Item To Steal?")
        print("0 = Oks na 'to")

        choice = input("Stealing What?: ")

        if choice == "0":
            break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(items):
            print("Don't steal something you can't have.")
            continue

        item = items[int(choice) - 1]

        name, weight, value = item

        if total_weight + weight > MAX_WEIGHT:
            print("Not enough remaining weights for this item.")
        else:
            chosen.append(item)
            total_weight += weight
            total_value += value
            print(f"{name} added.")

    return chosen, total_weight, total_value


def show_result(chosen, weight, value):
    print('')
    if not chosen:
        print("No items selected.")
    else:
        print("Items Taken:")
        for item in chosen:
            print(f"- {item[0]} (Weight: {item[1]}, Value: ₱{item[2]})")
    print(f"Total Weight: {weight}/{MAX_WEIGHT}")
    print(f"Total Value: ₱{value}")


def menu():
    while True:
        print("\nROBBERY BOB")
        print("\n1. Steal in House")
        print("2. Live a Good Life with Her\n")
        choice = input("Choose an option: ")

        if choice == "1":
            chosen, weight, value = manual_selection()
            show_result(chosen, weight, value)

        elif choice == "2":
            print(
                "You married her, have a family, visit 20 countries, eat different foods, see your kids together... happy with their own family."
            )
            break

        else:
            print("You make Noises! You got caught.")


menu()