a,b = input().split()
a = int(a)
b = int(b)

result = 0

if a%2 == 0:
    if b <= a//2:
        result = ((b-1)*2)+1
    else:
        result = (b - (a//2))*2
else:
    if b <= (a//2)+1:
        result = ((b-1)*2)+1
    else:
        result = (b-((a//2)+1))*2

print(result)
