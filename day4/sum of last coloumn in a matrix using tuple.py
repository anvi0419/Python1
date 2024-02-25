#write a python program to print the sum of last coloumn in a matrix using tuple
r,c=int(input()),int(input())
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    for j in i:
       sum+=i[c-1]
print(sum)
