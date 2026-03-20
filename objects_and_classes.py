"""
    OBJECTS AND CLASSES IN PYTHON
    Student: Naserian
    Unit: Object Oriented Programming
    Lecturer: Mr. Ochieng
    Institution: Technical University of Kenya (TUK)
"""


"""
    A CLASS is a blueprint that defines structure and behavior.
    An OBJECT is a specific instance created from that blueprint.
    Example: Class = Student ID card template, Object = Naserian's actual ID card.
"""

# --- 1. DEFINING A CLASS ---

class Student:
    
    university = "Technical University of Kenya"  # class attribute (shared by all)

    def __init__(self, name, reg_no, course):
        self.name = name          # instance attributes (unique to each)
        self.reg_no = reg_no
        self.course = course
        self.units = []

    def greet(self):
        return f"Hi, I'm {self.name} studying {self.course} at TUK."

    def register_unit(self, unit):
        self.units.append(unit)
        return f"{self.name} registered for '{unit}'."

    def show_units(self):
        if self.units:
            return f"{self.name}'s units: {', '.join(self.units)}"
        return f"{self.name} has not registered any units yet."

    def __str__(self):
        return f"Student(name='{self.name}', reg='{self.reg_no}', course='{self.course}')"


# --- 2. CREATING OBJECTS ---

print("=" * 50)
print("  CREATING AND USING OBJECTS")
print("=" * 50)

naserian = Student("Naserian", "CS/2025/001", "Computer Science")
kamau = Student("Kamau", "CS/2025/042", "Computer Science")
akinyi = Student("Akinyi", "IT/2025/015", "Information Technology")

print(f"\n{naserian.greet()}")
print(f"{kamau.greet()}")

print(naserian.register_unit("Object Oriented Programming"))
print(naserian.register_unit("Data Structures"))
print(naserian.show_units())
print(kamau.show_units())

print(f"\nAll attend: {Student.university}")
print(f"naserian is kamau? {naserian is kamau}")  # False - separate objects


# --- 3. INHERITANCE ---

print("\n" + "=" * 50)
print("  INHERITANCE")
print("=" * 50)


class Postgraduate(Student):
    """Extends Student with research features."""

    def __init__(self, name, reg_no, course, research_topic):
        super().__init__(name, reg_no, course)
        self.research_topic = research_topic

    def research(self):
        return f"{self.name} is researching: '{self.research_topic}'"

    def greet(self):  # overrides parent method
        return f"Hi, I'm {self.name}, a postgrad at TUK researching '{self.research_topic}'."


naserian_pg = Postgraduate("Naserian", "PG/2028/001", "Computer Science", "AI in Agriculture")

print(f"\n{naserian_pg.greet()}")
print(naserian_pg.research())
print(naserian_pg.register_unit("Advanced Algorithms"))  # inherited from Student
print(f"Is Postgraduate also a Student? {isinstance(naserian_pg, Student)}")  # True


# --- 4. ENCAPSULATION ---

print("\n" + "=" * 50)
print("  ENCAPSULATION")
print("=" * 50)


class StudentWallet:
    """Controls access to a student's M-Pesa wallet balance."""

    def __init__(self, owner, balance=0):
        self.owner = owner            # public
        self._bank = "M-Pesa"         # protected (convention)
        self.__balance = balance       # private (cannot access directly)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited KSh {amount}. Balance: KSh {self.__balance}"
        return "Amount must be positive."

    def pay_fees(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Paid KSh {amount} fees. Remaining: KSh {self.__balance}"
        return "Insufficient funds."

    def check_balance(self):
        return self.__balance


wallet = StudentWallet("Naserian", 15000)
print(f"\nOwner: {wallet.owner}")
print(f"Balance: KSh {wallet.check_balance()}")
print(wallet.deposit(5000))
print(wallet.pay_fees(8000))
# print(wallet.__balance)  # ERROR - private attribute!


# --- 5. KEY TAKEAWAYS ---

print("\n" + "=" * 50)
print("  KEY TAKEAWAYS")
print("=" * 50)
print("""
 - A CLASS is the blueprint (Student ID card template).
 - An OBJECT is a real instance (Naserian's actual ID).
 - INHERITANCE lets a child class extend a parent
   (Postgraduate extends Student).
 - ENCAPSULATION hides internal data and controls access
   (wallet balance cannot be changed directly).
 - Each object is independent - Naserian's units
   do not affect Kamau's or Akinyi's.
""")