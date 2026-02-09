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

Hey Lady Gaga, you’re invited to dinner at my place. It would be awesome to have you there!
Hey Steve Jobs, you’re invited to dinner at my place. It would be awesome to have you there!
Hey Betty White, you’re invited to dinner at my place. It would be awesome to have you there!

Good news — I found a bigger dinner table, so I can invite more people!

Hey Betty White, you’re invited to dinner at my place. I’m excited to have you join!
Hey Dolly Parton, you’re invited to dinner at my place. I’m excited to have you join!
Hey Elon Musk, you’re invited to dinner at my place. I’m excited to have you join!
Hey Lady Gaga, you’re invited to dinner at my place. I’m excited to have you join!
Hey Robin Williams, you’re invited to dinner at my place. I’m excited to have you join!
Hey Steve Jobs, you’re invited to dinner at my place. I’m excited to have you join!
