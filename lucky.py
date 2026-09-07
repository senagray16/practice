x = int(input())
lucky = ["4","7","44","77","47","74","444","447","474","477","744","747","774","777"]

a = 0
for i in lucky:
    if x%int(i)==0:
        a = 1
        break
    else:
        continue

if a==1:
    print("YES")
else:
    print("NO")




