Name="Astha"
marks=[85,90,78]
Subjects=("Math","Science","English")

Student={"name": Name,"age": 20}
hobbies={"reading","music","reading"}
print(Name.upper())
marks.append(88)
print(marks)
print(Subjects[0])

Student["marks"]=marks
print(Student)
hobbies.add("sports")
print(hobbies)
avg=sum(marks)/len(marks)
print("Average marks=",avg)