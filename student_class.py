# ============================================================
# Student Class — Object-Oriented Programming in Python
# Topics: class, __init__, instance methods, self keyword
# ============================================================


class Student:
    """
    A class to represent a student.

    Attributes
    ----------
    name : str
        Full name of the student.
    roll_number : int
        Unique roll number assigned to the student.
    marks : dict
        A dictionary mapping subject names to marks obtained.
    """

    # ----------------------------------------------------------
    # Constructor (__init__): called automatically when we
    # create a new Student object.
    # ----------------------------------------------------------
    def __init__(self, name: str, roll_number: int, marks: dict):
        """Initialize a Student with name, roll number, and marks."""
        self.name = name                # instance variable for name
        self.roll_number = roll_number  # instance variable for roll number
        self.marks = marks              # instance variable for marks (dict)

    # ----------------------------------------------------------
    # Display method: prints student details in a readable format
    # ----------------------------------------------------------
    def display(self):
        """Display all details of the student."""
        print("=" * 45)
        print(f"  Student Name   : {self.name}")
        print(f"  Roll Number    : {self.roll_number}")
        print(f"  Marks          :")
        for subject, mark in self.marks.items():
            print(f"      {subject:<12} : {mark}")
        total = sum(self.marks.values())
        average = total / len(self.marks) if self.marks else 0
        print(f"  Total Marks    : {total}")
        print(f"  Average Marks  : {average:.2f}")
        print("=" * 45)

    # ----------------------------------------------------------
    # Update methods: modify individual attributes after creation
    # ----------------------------------------------------------
    def update_name(self, new_name: str):
        """Update the student's name."""
        old_name = self.name
        self.name = new_name
        print(f"  [OK] Name updated: '{old_name}' -> '{new_name}'")

    def update_roll_number(self, new_roll: int):
        """Update the student's roll number."""
        old_roll = self.roll_number
        self.roll_number = new_roll
        print(f"  [OK] Roll number updated: {old_roll} -> {new_roll}")

    def update_marks(self, subject: str, new_mark: int):
        """Update marks for a specific subject (adds it if new)."""
        if subject in self.marks:
            old_mark = self.marks[subject]
            self.marks[subject] = new_mark
            print(f"  [OK] {subject} marks updated: {old_mark} -> {new_mark}")
        else:
            self.marks[subject] = new_mark
            print(f"  [OK] New subject added: {subject} = {new_mark}")


# ============================================================
# --- Using the Student class ---
# ============================================================

# 1. Create a Student object
student1 = Student(
    name="Akshaya",
    roll_number=101,
    marks={"Maths": 95, "Science": 88, "English": 92}
)

# 2. Display initial details
print("\n--- Initial Student Details ---")
student1.display()

# 3. Update the student's name
print("\n--- Updating student info... ---")
student1.update_name("Akshaya R")

# 4. Update roll number
student1.update_roll_number(201)

# 5. Update marks for an existing subject
student1.update_marks("Science", 94)

# 6. Add marks for a new subject
student1.update_marks("Computer Science", 99)

# 7. Display updated details
print("\n--- Updated Student Details ---")
student1.display()

# 8. Create a second student to show reusability
student2 = Student("Ravi", 102, {"Maths": 78, "Science": 82, "English": 85})
print("\n--- Another Student ---")
student2.display()
