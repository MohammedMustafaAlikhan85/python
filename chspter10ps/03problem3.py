class Demo:
    a = 4

o = Demo()
print(o.a)# Prints the class attribute because instance attritube is not present
o.a = 0 # Instance attritube is set
print(o.a)# Prints the instance attritube because instance attitube is present
print(Demo.a)#Prints the class attitube
