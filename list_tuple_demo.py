# ============================================
# 📊 Student Grade Analyzer using Lists & Tuples
# ============================================

# Tuples store fixed student records (name, grade)
# Lists store collections we can modify

# --- Student records as tuples (immutable) ---
students = [
    ("Alice", 92),
    ("Bob", 78),
    ("Charlie", 85),
    ("Diana", 95),
    ("Ethan", 60),
]

# --- Extract names and grades into separate lists ---
names = [student[0] for student in students]       # list comprehension
grades = [student[1] for student in students]

# --- Basic stats ---
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

print("=" * 40)
print("   🎓 CLASS GRADE REPORT")
print("=" * 40)

for name, grade in students:          # tuple unpacking in a loop
    status = "✅ Pass" if grade >= 70 else "❌ Fail"
    print(f"  {name:<10} | {grade}  | {status}")

print("-" * 40)
print(f"  Average Grade : {average:.1f}")
print(f"  Highest Grade : {highest} ({names[grades.index(highest)]})")
print(f"  Lowest Grade  : {lowest} ({names[grades.index(lowest)]})")
print("=" * 40)

# --- Bonus: sort students by grade (descending) ---
ranked = sorted(students, key=lambda s: s[1], reverse=True)

print("\n📋 Ranked List:")
for rank, (name, grade) in enumerate(ranked, start=1):
    print(f"  #{rank} {name} - {grade}")
