#write a python program to print keys and values of a dictionary
n=int(input("enter the no.of items:"))
d={}
for i in range(n):
    key=input("key: ")
    value=input("value: ")
    d[key]=value
for i in d:
    print("key:",i," ","value:",d[i])#if we need spaces we usecomma(,)in print statement
    print(f"key:[i]value:{d[i]}")#if we dont need space we use f in print statement
    print("key:{} value:{}".format(i,d[i]))#format print statement
for i in d.keys():#to print keys using methods
    print(i)
for i in d.values():#to print valuse using methods
    print(i)
