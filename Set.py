# 1. Creating sets (notice how duplicates are automatically removed)
wizard_it = {"Alice", "Bob", "Charlie", "Alice"}
cyber_security = {"Charlie", "David", "Elena", "Bob"}

print(f"IT Team: {wizard_it}")  # 'Alice' will only appear once
print(f"Security Team: {cyber_security}\n")

# 2. Finding common members (Intersection)
both_teams = wizard_it.intersection(cyber_security)
# Alternative syntax: both_teams = wizard_it & cyber_security
print(f"People in both teams: {both_teams}")

# 3. Combining everyone together (Union)
all_employees = wizard_it.union(cyber_security)
# Alternative syntax: all_employees = wizard_it | cyber_security
print(f"All unique employees: {all_employees}")

# 4. Finding who is ONLY in IT (Difference)
only_it = wizard_it.difference(cyber_security)
# Alternative syntax: only_it = wizard_it - cyber_security
print(f"Employees only in IT: {only_it}")

# 5. Adding and removing items
wizard_it.add("Frank")
wizard_it.discard("Alice")  # Safely removes 'Alice' if she exists
