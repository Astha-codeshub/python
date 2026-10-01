S="Hello"
print(S[1:4])
print(S+"World")
print(S[0])

lst=[1,2,3]
lst.append(4)
print(lst)
print("Slicing:", lst[1:3])

t=(1,2,3)
print(t[0])
print("Slicing:",t[1:3])
print("concatenation:",t+(5,6))
print("Repetition:",t*2)

d={"name":"Astha" ,"age" :"20"}
print("Access using key:",d["name"])

s1={1,2,3}
s2={3,4,5}
print("Set1:",s1)
print("Set2:",s2)
print("Union:",s1|s2)
print("Intersection:",s1&s2)