import random

responses = [
    "Yes, absolutely!", 
    "No way.", 
    "Maybe someday.", 
    "I'm not sure, ask again later."
]


print("--- Welcome to the Magic 8-Ball ---")
question = input("Ask a yes or no question: ")

answer = random.choice(responses)

print(f"\nYou asked: '{question}'")
print(f"The Magic 8-Ball says: {answer}")