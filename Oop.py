# 1. We define the blueprint (The Class)
class Dog:
    # This sets up the characteristics every dog will have
    def __init__(self, name, breed):
        self.name = name  # Every dog gets a name
        self.breed = breed  # Every dog gets a breed

    # This is an action the dog can do (A Method)
    def bark(self):
        return f"{self.name} says Woof!"


# 2. We use the blueprint to create actual dogs (The Objects)
dog1 = Dog(name="Buddy", breed="Golden Retriever")
dog2 = Dog(name="Luna", breed="Husky")

# 3. We look at their details and make them do actions
print(dog1.name)  # Output: Buddy
print(dog2.breed)  # Output: Husky

print(dog1.bark())  # Output: Buddy says Woof!
print(dog2.bark())  # Output: Luna says Woof!
