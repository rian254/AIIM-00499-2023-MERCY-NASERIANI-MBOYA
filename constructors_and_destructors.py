"""
    CONSTRUCTORS AND DESTRUCTORS IN PYTHON
    Student: Naserian
    Unit: Object Oriented Programming
    Lecturer: Mr. Ochieng
    Institution: Technical University of Kenya (TUK)
"""

# CONSTRUCTOR (__init__) - Called automatically when an object is CREATED.
# DESTRUCTOR  (__del__)  - Called automatically when an object is DESTROYED.
# Think of it like:
#   Constructor = Beginning of semester (set everything up)
#   Destructor  = End of semester (clean everything up)

import time


# --- 1. THE CONSTRUCTOR ---

print("=" * 50)
print("  PART 1: CONSTRUCTORS (__init__)")
print("=" * 50)


class UnitRegistration:
    """Constructor fires automatically when Naserian registers a unit."""

    def __init__(self, student_name, unit_name, lecturer):
        print(f"  [CONSTRUCTOR] {student_name} registered for {unit_name}")
        self.student_name = student_name
        self.unit_name = unit_name
        self.lecturer = lecturer
        self.cats_done = 0

    def do_cat(self):
        self.cats_done += 1
        return f"{self.student_name} completed CAT {self.cats_done} in {self.unit_name}"

    def info(self):
        return f"{self.student_name} | {self.unit_name} | Lecturer: {self.lecturer} | CATs: {self.cats_done}"


print("\nNaserian registers for units (constructor fires automatically):\n")
oop = UnitRegistration("Naserian", "Object Oriented Programming", "Mr. Ochieng")
dsa = UnitRegistration("Naserian", "Data Structures", "Dr. Wanjiku")

print(oop.do_cat())
print(oop.do_cat())
print(f"\n  {oop.info()}")
print(f"  {dsa.info()}")


# --- 2. CONSTRUCTOR WITH DEFAULT VALUES ---

print("\n" + "=" * 50)
print("  PART 2: CONSTRUCTOR WITH DEFAULTS")
print("=" * 50)


class CampusWifi:
    """Constructor with default parameters - TUK Wi-Fi."""

    def __init__(self, student_name, network="TUK-WiFi", lab="Main Lab"):
        print(f"  [CONSTRUCTOR] {student_name} connected to {network} in {lab}")
        self.student_name = student_name
        self.network = network
        self.lab = lab
        self.connected = True

    def status(self):
        state = "Online" if self.connected else "Offline"
        return f"  {self.student_name} on '{self.network}' ({self.lab}) - {state}"


print("\nUsing defaults:")
conn1 = CampusWifi("Naserian")
print(conn1.status())

print("\nCustom values:")
conn2 = CampusWifi("Naserian", network="TUK-Library", lab="Library")
print(conn2.status())


# --- 3. THE DESTRUCTOR ---

print("\n" + "=" * 50)
print("  PART 3: DESTRUCTORS (__del__)")
print("=" * 50)


class LockerRental:
    """Constructor sets up the locker, destructor releases it."""

    def __init__(self, student_name, locker_number):
        print(f"\n  [CONSTRUCTOR] {student_name} rented Locker #{locker_number}")
        self.student_name = student_name
        self.locker_number = locker_number
        self.items = []

    def store(self, item):
        self.items.append(item)
        return f"  Stored '{item}' in Locker #{self.locker_number}"

    def __del__(self):
        if hasattr(self, "locker_number"):
            print(f"  [DESTRUCTOR]  Locker #{self.locker_number} returned by {self.student_name}")


print("\n--- Naserian rents a locker ---")
locker = LockerRental("Naserian", 105)
print(locker.store("Textbooks"))
print(locker.store("Lab coat"))

print("\n--- Semester ends - locker returned ---")
del locker  # triggers __del__


# --- 4. REAL-WORLD: COMPUTER LAB SESSIONS ---

print("\n" + "=" * 50)
print("  PART 4: COMPUTER LAB SESSIONS")
print("=" * 50)


class LabSession:
    """Tracks who is using TUK computer lab workstations."""

    capacity = 30
    occupied = 0

    def __init__(self, student_name, workstation):
        self.student_name = student_name
        self.workstation = workstation
        self.active = True
        LabSession.occupied += 1
        free = LabSession.capacity - LabSession.occupied
        print(f"\n  [CONSTRUCTOR] {student_name} logged into PC {workstation}")
        print(f"               Occupied: {LabSession.occupied} | Free: {free}")

    def run_code(self, filename):
        return f"  {self.student_name} running '{filename}' on PC {self.workstation}"

    def __del__(self):
        if hasattr(self, "active") and self.active:
            self.active = False
            LabSession.occupied -= 1
            free = LabSession.capacity - LabSession.occupied
            print(f"  [DESTRUCTOR]  {self.student_name} logged out of PC {self.workstation}")
            print(f"               Occupied: {LabSession.occupied} | Free: {free}")


print("\n--- Students enter the lab ---")
s1 = LabSession("Naserian", 5)
s2 = LabSession("Kamau", 6)
s3 = LabSession("Akinyi", 7)

print(f"\n{s1.run_code('oop_assignment.py')}")

print("\n--- Students leave ---")
del s1
del s2
del s3


# --- 5. LIFECYCLE: SEMESTER START TO END ---

print("\n" + "=" * 50)
print("  PART 5: OBJECT LIFECYCLE")
print("=" * 50)


class Semester:
    """Watch an object from creation to destruction."""

    def __init__(self, student_name, semester):
        self.student_name = student_name
        self.semester = semester
        print(f"  [CREATED]   {student_name} started {semester}")

    def attend(self, unit):
        print(f"  [ACTIVE]    {self.student_name} attending {unit}")

    def __del__(self):
        if hasattr(self, "student_name"):
            print(f"  [DESTROYED] {self.student_name}'s {self.semester} ended")


print()
sem = Semester("Naserian", "Semester 1, 2025/2026")
sem.attend("Object Oriented Programming")
sem.attend("Data Structures")
del sem

print()


def short_semester():
    temp = Semester("Naserian", "Semester 2, 2025/2026")
    temp.attend("Software Engineering")
    print("  [SCOPE]     Function ending - object destroyed automatically")

short_semester()


# --- 6. KEY TAKEAWAYS ---

print("\n" + "=" * 50)
print("  KEY TAKEAWAYS")
print("=" * 50)
print("""
 CONSTRUCTOR (__init__):
  - Runs automatically when an object is created.
  - Like registering for a unit - sets up everything.
  - Can accept parameters with default values.
  - Every class should have one.

 DESTRUCTOR (__del__):
  - Runs automatically when an object is destroyed.
  - Like end of semester - clean up resources.
  - Triggered by 'del obj' or when object goes out of scope.
  - For reliable cleanup, prefer context managers:
      with open("naserian_notes.txt") as f:
          notes = f.read()
      # file closed automatically - no destructor needed
""")
