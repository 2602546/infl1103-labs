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


inventory = 0
f = 0

while True:
    result = get_valid_input()

    if result == "quit":
        generate_report(inventory, f)
        break
    elif result is None:
        f += 1
    else:
        inventory = process_delivery(inventory, result)
        tax = calculate_tax(result)

        if inventory > 500:
            print("Alert: Overstock")
            generate_report(inventory, f)
            break