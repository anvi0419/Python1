#write a python program to print sum of numbers using recursion
def printing(n):
    if n<1:
        return 1
    else:
        print(n)
        return n+printing(n-1)
n=int(input())
sum=printing(n)
print(sum)
