# 6-9. Favorite Places

favorite_places = {
    "Ethan": ["London", "Asheville", "New York"],
    "Natalie": ["Paris", "Miami"],
    "Hayden": ["Tokyo", "Los Angeles", "Denver"]
}

# Loop through the dictionary
for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places are:")
    
    for place in places:
        print(f"- {place}")

  Ethan's favorite places are:
- London
- Asheville
- New York

Natalie's favorite places are:
- Paris
- Miami

Hayden's favorite places are:
- Tokyo
- Los Angeles
- Denver
