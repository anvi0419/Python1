s=input()
s1="codeforces"
c=0
for i in range (len(s)):
    if s[i]!=s1[i]:
        c+=1
print(c)
