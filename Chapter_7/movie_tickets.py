# 7-5. Movie Tickets

print("Welcome to the Movie Theater!")

# Ask how many tickets
num_tickets = int(input("How many tickets would you like to purchase? "))

total_cost = 0

# Loop to ask for each person's age
for i in range(num_tickets):
    age = int(input(f"Enter the age of ticket holder #{i + 1}: "))

    if age < 3:
        print("Ticket is free.")
        total_cost += 0
    elif age <= 12:
        print("Ticket costs $10.")
        total_cost += 10
    else:
        print("Ticket costs $15.")
        total_cost += 15

print(f"\nTotal cost for all tickets: ${total_cost}")

Welcome to the Movie Theater!
How many tickets would you like to purchase? 3
Enter the age of ticket holder #1: 2
Ticket is free.
Enter the age of ticket holder #2: 8
Ticket costs $10.
Enter the age of ticket holder #3: 16
Ticket costs $15.

Total cost for all tickets: $25
