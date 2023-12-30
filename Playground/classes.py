class Student:
    def __init__(self) -> None:
        self.name = "Mahesh"
        self.age = 26
        self.race = "Asian"
        self.IsVeteran = False
    
    def getName(self) -> str:
        return self.name
    
    def getAge(self) -> int:
        return self.age
    
    def getRace(self) -> int:
        return self.race

student = Student()
print("Student name is:", student.getName())
print("Student age is:", student.getAge())
print("Is Veteran flag is:", student.IsVeteran)