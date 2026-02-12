# 3-8. My Updated Guest List - Sorted

guests = ["Lady Gaga", "Steve Jobs", "Betty White"]

# Original invitations
for person in guests:
    print(f"Hey {person}, you’re invited to dinner at my place. It would be awesome to have you there!")

print("\nGood news — I found a bigger dinner table, so I can invite more people!\n")

# Add 3 more guests
guests.insert(0, "Dolly Parton")               # beginning
guests.insert(len(guests)//2, "Robin Williams") # middle
guests.append("Elon Musk")                    # end

# Sort the list alphabetically
guests.sort()

# New invitations (sorted)
for person in guests:
    print(f"Hey {person}, you’re invited to dinner at my place. I’m excited to have you join!")

    print("\nThe first three items in the list are:")
print(guests[:3])

print("\nThree items from the middle of the list are:")
print(guests[2:5])

print("\nThe last three items in the list are:")
print(guests[-3:])

The first three items in the list are:
Hey Dolly Parton, you’re invited to dinner at my place. I’m excited to have you join!

The first three items in the list are:
Hey Elon Musk, you’re invited to dinner at my place. I’m excited to have you join!

The first three items in the list are:
Hey Lady Gaga, you’re invited to dinner at my place. I’m excited to have you join!

The first three items in the list are:
Hey Robin Williams, you’re invited to dinner at my place. I’m excited to have you join!

The first three items in the list are:
Hey Steve Jobs, you’re invited to dinner at my place. I’m excited to have you join!

The first three items in the list are:
['Betty White', 'Dolly Parton', 'Elon Musk']

Three items from the middle of the list are:
['Elon Musk', 'Lady Gaga', 'Robin Williams']

The last three items in the list are:
['Lady Gaga', 'Robin Williams', 'Steve Jobs']
