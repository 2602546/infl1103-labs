def load_inventory():
    try:
        file = open("inventory.txt", "r")
        lines = file.readlines()
        file.close()
        total = int(lines[0])
        history = [int(x) for x in lines[1:]]
        return total, history
    except FileNotFoundError:
        return 0, []


def get_valid_input():
    s = input("Enter stock quantity or quit: ")

    if s == "quit":
        return "quit"
    elif not s.isdigit():
        print("Error: Invalid input")
        return None
    else:
        n = int(s)
        if n < 0:
            print("Error: Negative numbers are not allowed")
            return None
        return n


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


inventory, history = load_inventory()
f = 0

while True:
    result = get_valid_input()

    if result == "quit":
        generate_report(inventory, f)
        print(history)
        break
    elif result is None:
        f += 1
    else:
        inventory = process_delivery(inventory, result)
        history.append(result)
        tax = calculate_tax(result)

        if inventory > 500:
            print("Alert: Overstock")
            generate_report(inventory, f)
            print(history)
            break