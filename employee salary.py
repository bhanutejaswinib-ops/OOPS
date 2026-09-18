class employee:
    Employee_Name = "Srinidhi"
    Employee_ID = "50505"
    salary=10000000000
    def total_salary(self):
        HRA = 0.2*self.salary
        DA=0.1*self.salary
        Total_amount = HRA + DA + self.salary
        print(Total_amount)
e=employee()
e.total_salary()