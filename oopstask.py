
#question
"""
Write a Python program to calculate and display the grade of a student
using Class and Objects.
Requirements:
1. Create a class Student with:
An __init__ method to initialize the name and marks of a student.
A method display_grade() that:
Assigns a grade according to:
Marks >= 90 → Grade A
Marks >= 75 and < 90 → Grade B
Marks >= 50 and < 75 → Grade C
Marks < 50 → Fail
Prints the student's name and grade.

"""

#answer
"""
class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def display_grade(self):
        if self.marks>=90:
            grade="A"
        elif self.marks>=75 and self.marks<90:
            grade="B"
        elif self.marks>=50 and self.marks<75:
            grade = "C"
        else:
            grade ="Fail"
        print(f"{self.name}:Grade:{grade}")
student1=Student("alice",89)
student1.display_grade()
student2=Student("jhon",95)
student2.display_grade()
"""




#question2
"""
Write a Python program to calculate the average grade of a student
across multiple subjects using Class and Objects.
Requirements:
1. Create a class Student with:
OOP Questions 1
An __init__ method to initialize name and a dictionary marks with subject
names and scores.
A method calculate_average() to compute the average marks.
A method display_grade() that:
Assigns a grade based on the average:
Average >= 90 → Grade A
Average >= 75 and < 90 → Grade B
Average >= 50 and < 75 → Grade C
Average < 50 → Fail
Prints the student's name, average marks, and grade.
2. Create at least two student objects with multiple subject marks.
3. Call the display_grade() method for each object
"""
#answer
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        if not self.marks:
            return 0
        total = sum(self.marks.values())
        return total / len(self.marks)
    
    def display_grade(self):
        average=self.calculate_average()
        if average >= 90:
            grade = 'A'
        elif average >= 75<90:
            grade = 'B'
        elif average >= 50<75:
            grade = 'C'
        else:
            grade = 'Fail'
        print(f"{self.name} Average:{average:.1f}|Grade:{grade}")
student1 = Student("Alice",{
    "Math": 85,
    "Science": 78,
    "English": 84
})
student2 = Student("John",{
    "Math": 95,
    "Science": 92,
    "English": 86
})

student1.display_grade()
student2.display_grade()
"""

