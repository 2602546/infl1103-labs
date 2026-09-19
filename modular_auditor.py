inventory = 0
f = 0

while True:
inventory = 0
f = 0

while True:
    s = input("Enter stock quantity or quit: ")

    if s == "quit":
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries:", f)
        break
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries:", f)
        break
    elif not s.isdigit():
        print("Error: Invalid input")
        f += 1
        f += 1
    else:
        n = int(s)


        if n < 0:
            print("Error: Negative numbers are not allowed")
            f += 1
        else:
            inventory += n
            f += 1
        else:
            inventory += n

            if inventory > 500:
                print("Alert: Overstock")
                break

            if inventory > 500:
                print("Alert: Overstock")
                break