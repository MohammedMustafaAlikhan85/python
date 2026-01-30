class Employee :
    language ="Python"#this is a class attribute
    salary = 1200000

    def getinfo(self):
        print(f"The language is{self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet ():
        print("Good morning")


harry = Employee()
#harry.language="JavaScript"#this is an instance attribute
harry.greet()
harry.getinfo()
#Employee.getinfo(harry)
