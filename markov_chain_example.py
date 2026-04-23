import numpy as np

states = ["Sunny", "Cloudy", "Rainy"]

P = np.array([
    [0.6, 0.3, 0.1], 
    [0.4, 0.3, 0.3],  
    [0.2, 0.4, 0.4]  
])

def simulate_weather(start_state, days, P, states):
    idx = states.index(start_state)
    sequence = [start_state]
    for _ in range(days - 1):
        idx = np.random.choice(len(states), p=P[idx])
        sequence.append(states[idx])
    return sequence
result = simulate_weather("Sunny", 8, P, states)
print("Weather Forecast:", result)