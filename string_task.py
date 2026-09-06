ia = input()
b = ""
for i in ia:
    if not(i.upper() in ["A", "O", "Y", "E", "U", "I"]):
        b = b + "." + i

b = b.lower()

print(b)
