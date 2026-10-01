def add(a,b):
    return a+b

print("Sum:",add(2,3))

def student(name,age):
    print("Name:",name)
    print("Age:",age)

student(age=20,name="Astha")

def greet(name="Guest"):
    print("Hello",name)

greet()
greet("Astha")

def total(*numbers):
    return sum(numbers)
print("Total:",total(1,2,3,4))

def details(**info):
    for key,value in info.items():
        print(key,":",value)

details(name="Astha",age=20)