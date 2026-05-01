fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

print("Original Dictionary:", fruit_colors)

print("\nThe color of a banana is:", fruit_colors["banana"])

fruit_colors["watermelon"] = "green"
print("\nAfter adding watermelon:", fruit_colors)

fruit_colors["apple"] = "green"  
print("\nAfter changing apple's color:", fruit_colors)

del fruit_colors["grape"]
print("\nAfter removing grape:", fruit_colors)

if "banana" in fruit_colors:
    print("\nYes, banana is in our dictionary!")
