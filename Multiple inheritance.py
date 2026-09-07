class school:
    def staff(self):
        print("maths teacher")
class teacher:
    def maths(self):
        print("Teacher teaches maths")
class Student(school,teacher):
    def notebook(self):
        print("Student writes notes")
d1=Student()
d1.staff()
d1.maths()
d1.notebook()
    
    