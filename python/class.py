
class Employee:
  def __init__(self,name,salary):
    self.name=name
    self._salary=salary

  def display(self):
    print("Name:",self.name)
    print("Salary:",self._salary)


class Manager(Employee):
  def __init__(self,name,salary,bonus):
    super(). __init__(name,salary)
    self.bonus=bonus

  def total_salary(self):
    return self._salary+self.bonus
  
m=Manager("Astha",30000,5000)
m.display()
print("Bonus:",m.bonus)
print("Total Salary:",m.total_salary())



