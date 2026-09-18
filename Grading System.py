class Student:
    name="Srinidhi"
    Roll_number="59"
    English_marks = int(input())
    Maths_marks=int(input())
    physics_marks=int(input())
    def Total_marks(self):
        marks=self.English_marks + self.Maths_marks + self.physics_marks
        print(marks)
    def Average(self):
        avg=(self.English_marks + self.Maths_marks + self.physics_marks)/3
        print(avg)
    def grade(self):
        if((self.English_marks + self.Maths_marks + self.physics_marks)/3>=90):
            print("A")
        elif(89>(self.English_marks + self.Maths_marks + self.physics_marks)/3>76):
            print("B")
        elif(50>(self.English_marks + self.Maths_marks + self.physics_marks)/3>40):
            print("C")
        else:
            print("Fail")
s=Student()
s.Total_marks()
s.Average()
s.grade()
        
        
        