d={1:"welcome", 2:"to",3:"CSVTU"}  # 1 is 'key' and welcome is 'value'.     
'''print(d)
print(d[1])   
print("me" in d[1])   
print("em" in d[1])   '''



print("welcome" in d.values())   #dictionary only checks key
print("welcome" in d)