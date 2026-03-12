
students = []

def add_student(usn, name, section, subject_code, contact_no):
    """Add a student record with contact number at the end."""
    student = [usn, name, section, subject_code, contact_no]
    students.append(student)
    print(f"✅ Student '{name}' added successfully!")

def display_students():
    """Display all student records in a formatted table."""
    if not students:
        print("No student records found.\n")
        return

    print("\n" + "=" * 85)
    print(f"{'Index':<6} {'USN':<15} {'Name':<20} {'Section':<10} {'Subject':<12} {'Faculty':<15} {'Contact'}")
    print("=" * 85)
    for i, s in enumerate(students):
        print(f"{i:<6} {s[0]:<15} {s[1]:<20} {s[2]:<10} {s[3]:<12} {s[4] if len(s) > 4 else 'N/A':<15} {s[5] if len(s) > 5 else 'N/A'}")
    print("=" * 85)
    print(f"Total Records: {len(students)}\n")

# ── 1. Add students (USN, Name, Section, Subject Code, Contact No) ──────────
print("=" * 50)
print("       STUDENT RECORD MANAGEMENT SYSTEM")
print("=" * 50)

add_student("1RV21CS001", "Alice Johnson",  "A", "CS101", "9876543210")
add_student("1RV21CS002", "Bob Smith",      "B", "CS102", "9876543211")
add_student("1RV21CS003", "Carol Williams", "A", "CS103", "9876543212")
add_student("1RV21CS004", "David Brown",    "C", "CS101", "9876543213")
add_student("1RV21CS005", "Eva Martinez",   "B", "CS104", "9876543214")

print("\n📋 Initial Student Records (with Contact No at end):")
display_students()

# ── 2. Remove subject code (index 3) from all records ───────────────────────
print("🗑️  Removing 'Subject Code' from all records...")
for s in students:
    s.pop(3)   # subject_code was at index 3

print("\n📋 After Removing Subject Code:")
print(f"{'Index':<6} {'USN':<15} {'Name':<20} {'Section':<10} {'Contact'}")
print("-" * 65)
for i, s in enumerate(students):
    print(f"{i:<6} {s[0]:<15} {s[1]:<20} {s[2]:<10} {s[3]}")
print()

# ── 3. Insert Faculty Name at index 3 (after Section) ───────────────────────
faculties = ["Dr. Smith", "Prof. Jones", "Dr. Smith", "Prof. Lee", "Prof. Jones"]

print("➕ Inserting 'Faculty Name' at index 3 (after Section)...")
for s, faculty in zip(students, faculties):
    s.insert(3, faculty)   # insert at index 3

print("\n📋 After Inserting Faculty Name at Index 3:")
print(f"{'Index':<6} {'USN':<15} {'Name':<20} {'Section':<10} {'Faculty':<15} {'Contact'}")
print("-" * 80)
for i, s in enumerate(students):
    print(f"{i:<6} {s[0]:<15} {s[1]:<20} {s[2]:<10} {s[3]:<15} {s[4]}")
print()

# ── 4. Replace index 0 value (USN) with "Python" in first record ─────────────
print("🔄 Replacing index 0 value (USN) of first record with 'Python'...")
students[0][0] = "Python"

print("\n📋 After Replacing Index 0 of First Record:")
print(f"{'Index':<6} {'USN/Val':<15} {'Name':<20} {'Section':<10} {'Faculty':<15} {'Contact'}")
print("-" * 80)
for i, s in enumerate(students):
    print(f"{i:<6} {s[0]:<15} {s[1]:<20} {s[2]:<10} {s[3]:<15} {s[4]}")
print()

# ── Summary of list operations used ─────────────────────────────────────────
print("=" * 50)
print("         LIST OPERATIONS SUMMARY")
print("=" * 50)
print("  append()  → Added contact_no at the end")
print("  pop(3)    → Removed subject code at index 3")
print("  insert(3) → Inserted faculty name at index 3")
print("  list[0]   → Replaced index 0 value with 'Python'")
print("=" * 50)