#write a python program to print sum of min and max element in a matrix using tuple
r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))
min,max=1000,0
print(tuple(l))
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
            if j<min:
                min=j
print(max+min)

