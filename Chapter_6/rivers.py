# 6-5. Rivers

# Create a dictionary of rivers and the countries they run through
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states"
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()  # blank line for cleaner output

# Print the name of each river
print("Rivers included:")
for river in rivers.keys():
    print(river.title())

print()  # blank line

# Print the name of each country
print("Countries included:")
for country in rivers.values():
    print(country.title())

The Nile runs through Egypt.
The Amazon runs through Brazil.
The Mississippi runs through United States.

Rivers included:
Nile
Amazon
Mississippi

Countries included:
Egypt
Brazil
United States
