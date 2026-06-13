# Function to calculate calories burned based on steps 
def calculate_calories(steps):
    calories_per_step = 0.04  # Average calories burned per step
    calories_burned = steps * calories_per_step
    return calories_burned

# Test the function with different step counts  
test_steps = [1000, 5000, 10000, 20000]
for steps in test_steps:
    calories = calculate_calories(steps)
    print(f"Steps: {steps}, Calories Burned: {calories:.2f}")  