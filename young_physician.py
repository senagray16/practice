n = int(input())
x=0
y=0
z=0


for i in range(n):
    xa,xb,xc = input().split()
    xa = int(xa)
    xb = int(xb)
    xc = int(xc)

    x += xa
    y += xb
    z += xc 

if x!=0 or y!=0 or z!=0:
    print("NO")
else:
    print("YES")   
