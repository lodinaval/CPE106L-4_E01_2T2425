"""
File: student.py
Resources to manage a student's name and test scores.
"""

import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
    
    def isEqual(self, otherStudent):
        """Returns true or false if the 2 objects are equal."""
        if(self.getAverage() == otherStudent.getAverage()):
            print(self.getName() + "'s score is equal to " + otherStudent.getName() + "'s score")
        else:
            print(self.getName() + "'s score is NOT equal to " + otherStudent.getName() + "'s score")

    def isLessThan(self, otherStudent):
        """Returns true or false if the 2 objects are equal."""
        if(self.getAverage() < otherStudent.getAverage()):
            print(self.getName() + "'s score is less than " + otherStudent.getName() + "'s score")
        else:
            print(self.getName() + "'s score is NOT less than " + otherStudent.getName() + "'s score")

    def isGreaterThan(self, otherStudent):
        """Returns true or false if the 2 objects are equal."""
        if(self.getAverage() >= otherStudent.getAverage()):
            print(self.getName() + "'s score is greater than or equal to " + otherStudent.getName() + "'s score")
        else:
            print(self.getName() + "'s score is NOT greater than or equal to " + otherStudent.getName() + "'s score")
        
    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """Define Students"""
    student1 = Student("Ken", 5)
    for i in range(1, 6):
        student1.setScore(i, 60)
    print(student1)
    student2 = Student("Barbara", 5)
    for i in range(1, 6):
        student2.setScore(i, 70)
    print(student2)
    student3 = Student("John", 5)
    for i in range(1, 6):
        student3.setScore(i, 100)
    print(student3)
    student4 = Student("Lizzy", 5)
    for i in range(1, 6):
        student4.setScore(i, 100)
    print(student4)

    #PROGRAMMING EX 1:
    print("EQUALITY TEST: ")
    student3.isEqual(student4) #t
    student1.isEqual(student3) #f

    print("LESS THAN TEST: ")
    student1.isLessThan(student2) #t
    student4.isLessThan(student1) #f
    student3.isLessThan(student4) #f

    print("GREATER THAN OR EQUAL TEST: ")
    student3.isGreaterThan(student4) #t
    student3.isGreaterThan(student1) #t
    student2.isGreaterThan(student4) #f

    print("------------------------")
    #PROGRAMMING EX 2:
    """Define Students"""
    studentA = Student("Ken", 5)
    for i in range(1, 6):
        studentA.setScore(i, 35)
    print(studentA)
    studentB = Student("Barbara", 5)
    for i in range(1, 6):
        studentB.setScore(i, 81)
    print(studentB)
    studentC = Student("John", 5)
    for i in range(1, 6):
        studentC.setScore(i, 67)
    print(studentC)
    studentD = Student("Lizzy", 5)
    for i in range(1, 6):
        studentD.setScore(i, 42)
    print(studentD)

    studentList = []
    studentList.append(studentA)
    studentList.append(studentB)
    studentList.append(studentC)
    studentList.append(studentD)

    print("\nSHUFFLED: ")
    random.shuffle(studentList)
    for student in studentList:
        print(student)
    
    print("\nSORTED: ")
    studentList.sort(key=lambda student: student.getAverage())
    for student in studentList:
        print(student)

if __name__ == "__main__":
    main()


