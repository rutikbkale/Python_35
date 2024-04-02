# WAP to implement a class person

class Person:
    def introduce(self):
        print("Hi i am a person.")

class Student(Person):
    def introduce(self):
        print("Hi i am a student.")

class Teacher(Person):
    def introduce(self):
        print("Hi i am a Teacher.")

obj1 = Student()
obj1.introduce()
obj2 = Teacher()
obj2.introduce()