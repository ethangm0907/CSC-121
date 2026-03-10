# 8-5. Cities

# Function with a default country
def describe_city(city, country="United States"):
    print(f"{city} is in {country}.")

# Call the function three times
describe_city("Asheville")
describe_city("New York")
describe_city("Reykjavik", "Iceland")

Asheville is in United States.
New York is in United States.
Reykjavik is in Iceland.
