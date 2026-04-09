# A simple program about lists!

# 1. Creating a list of relaxing activities to do after exams
relax_activities = ["Sleep for 10 hours", "Watch a movie", "Eat your favorite food", "Listen to music"]

print("Things to do after internals:")
# Looping through the list and printing each activity
for index, activity in enumerate(relax_activities, 1):
    print(f"{index}. {activity}")

print("\nWait, we forgot one thing! Let's add it.")
# 2. Adding an item to the end of the list using append()
relax_activities.append("Play some video games")

print("\nUpdated list of activities:")
print(relax_activities)

# 3. Getting the first activity from the list (Lists are 0-indexed)
print(f"\nThe very first thing you should do is: {relax_activities[0]}")
