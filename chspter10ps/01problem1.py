class Programmer :
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Harry",1200000,2450001)
print(p.name,p.salary,p.pin,p.company)
r = Programmer("Rajesh",1500000,2434001)
print(r.name,r.salary,r.pin,r.company)
