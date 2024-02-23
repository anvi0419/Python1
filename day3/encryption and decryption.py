#write a python program to make encryption and decryption with a key value using functions
def encrypt(s,k):
    s1=""
    for i in s:
        x1=ord(i)+k
        s1+=chr(x1)
    print(s1)
def decrypt(s,k):
    s1=""
    for i in s:
        x1=ord(i)-k
        s1+=chr(x1)
    print(s)
k=int(input("enter the key values:"))
s=input("enter string:")
o=input("select operstion:")
if o=="encrypt":
  encrypt(s,k)
elif o=="decrypt":
    decrypt(s,k)
else:
  print("error")
        

