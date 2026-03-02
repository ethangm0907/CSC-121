# 7-8. Deli Sandwiches

# List of sandwich orders
sandwich_orders = ["tuna", "ham", "turkey", "veggie", "blt"]

# Empty list for finished sandwiches
finished_sandwiches = []

# Make sandwiches until none are left
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made!")
print("Finished sandwiches:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

I made your blt sandwich.
I made your veggie sandwich.
I made your turkey sandwich.
I made your ham sandwich.
I made your tuna sandwich.

All sandwiches have been made!
Finished sandwiches:
- blt
- veggie
- turkey
- ham
- tuna
