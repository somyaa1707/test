class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  
    def get_marks(self):
        return self.__marks
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.__marks}"
