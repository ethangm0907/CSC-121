# 9-14. Lottery

import random

# List with numbers and letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "A", "B", "C", "D", "E"]

# Randomly select 4 numbers and 1 letter
winning_numbers = random.sample(lottery_pool, 5)

print("Winning lottery combination:", winning_numbers)

# Get user input
user_input = input("Enter your lottery guess (5 characters, no spaces): ")

# Convert user input into a list
user_list = list(user_input)

# Compare
if user_list == winning_numbers:
    print("You won the lottery!")
else:
    print("Sorry, you did not win.")

Winning lottery combination: [7, 4, 'A', 6, 'D']
Enter your lottery guess (5 characters, no spaces): 
