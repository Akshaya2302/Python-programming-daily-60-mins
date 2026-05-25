class Time:
    
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def add_time(self, t2):
        result = Time(0, 0, 0)

        result.second = self.second + t2.second
        result.minute = self.minute + t2.minute
        result.hour = self.hour + t2.hour

        if result.second >= 60:
            result.second -= 60
            result.minute += 1

        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1

        return result

    def display(self):
        print("%.2d:%.2d:%.2d" %
              (self.hour, self.minute, self.second))
# Creating objects
t1 = Time(10, 45, 50)
t2 = Time(2, 20, 30)

# Adding time
t3 = t1.add_time(t2)

# Display result
print("Time 1:")
t1.display()

print("Time 2:")
t2.display()

print("Added Time:")
t3.display()
