class Father:
    def __init__(self, father_name, father_occupation):
        self.father_name = father_name
        self.father_occupation = father_occupation

    def show_father_info(self):
        print(f"Father's Name: {self.father_name}")
        print(f"Father's Occupation: {self.father_occupation}")
class Mother:
    def __init__(self, mother_name, mother_occupation):
        self.mother_name = mother_name
        self.mother_occupation = mother_occupation
    def show_mother_info(self):
        print(f"Mother's Name: {self.mother_name}")
        print(f"Mother's Occupation: {self.mother_occupation}")
class Child(Father, Mother):
    def __init__(self, father_name, father_occupation, mother_name, mother_occupation, child_name, child_age):
        Father.__init__(self, father_name, father_occupation)
        Mother.__init__(self, mother_name, mother_occupation)
        self.child_name = child_name
        self.child_age = child_age
    def show_child_info(self):
        print(f"Child's Name: {self.child_name}")
        print(f"Child's Age: {self.child_age}")
        print("\n--- Parent Info ---")
        self.show_father_info()
        self.show_mother_info()
child = Child(
    father_name="John",
    father_occupation="Engineer",
    mother_name="Alice",
    mother_occupation="Doctor",
    child_name="Emma",
    child_age=10
)

child.show_child_info()
