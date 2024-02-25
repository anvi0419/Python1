#write a python program to print the sum of even palindrome in a range  and also print the list of palindrome
def palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return 1
    else:
        return 0
n,m=int(input()),int(input())
l1,l2=[],[]
for i in range(n,m+1):
    flag=palindrome(i)#flag is a variable it indicates the status of the given method 
    if flag==1:
        l1.append(i)
    if n%2==0:
       if flag==1:
          l2.append()
print(l1)
print(sum(l1))
    






    
 
