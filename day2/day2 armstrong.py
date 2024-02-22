#write a python program to check whether the given number is armstrong or not
n=int(input())
sum=n
rev=0
while n>0:
    digit=n%10
    rev=rev+digit**3
    n//=10
if rev==sum:
    print("armstrong num")
else:
    print("not an armstrong")
