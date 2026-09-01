a = input()

b = a[0]
c = 1
for i in a[1:]:
    if i == b:
        c+=1
    else:
        c = 1
        b = i

    if c == 7:
        break 

if c==7:
    print("YES")
else:
    print("NO")

