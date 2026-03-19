customers = []

while True:
    print("\n--- Hotel Management System ---")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Check-out & Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter customer name: ")
        
        print("Room Type:")
        print("1. AC (₹2000/day)")
        print("2. Non-AC (₹1000/day)")
        room_type = input("Choose room type: ")

        if room_type == '1':
            price = 2000
            room_name = "AC"
        else:
            price = 1000
            room_name = "Non-AC"

        days = int(input("Enter number of days: "))
        food = int(input("Enter food cost: "))

        total = (price * days) + food

        customers.append({
            "name": name,
            "room": room_name,
            "days": days,
            "food": food,
            "total": total
        })

        print("Customer added successfully!")

    elif choice == '2':
        if not customers:
            print("No customers found.")
        else:
            for i, c in enumerate(customers):
                print(f"{i+1}. {c['name']} | {c['room']} | {c['days']} days | Total ₹{c['total']}")

    elif choice == '3':
        num = int(input("Enter customer number to checkout: "))
        if 0 < num <= len(customers):
            c = customers.pop(num - 1)
            print("\n--- BILL ---")
            print(f"Name: {c['name']}")
            print(f"Room: {c['room']}")
            print(f"Days: {c['days']}")
            print(f"Food Cost: ₹{c['food']}")
            print(f"Total Bill: ₹{c['total']}")
        else:
            print("Invalid number")

    elif choice == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice")