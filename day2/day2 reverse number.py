#write the python program to print the reverse of a number
n=int(input())
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)


