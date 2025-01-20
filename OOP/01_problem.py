class Programmers:
    company = "Microsoft" 
    def __init__(self,name,salary,position):
        self.name = name 
        self.salary = salary 
        self.position = position 

Employee_1 = Programmers ("Taufiq", 1200000, "Junior developer")

print(Employee_1.company , Employee_1.name , Employee_1.salary , Employee_1.position)