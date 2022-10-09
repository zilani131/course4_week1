from ctypes.wintypes import CHAR

r=""
shift=int(4)
z=input("Enter your code ")
for char in z:
    a=(ord(char)-97)%26
    b=(a+shift)%26
   # print(b) #encrypted increase by 4
    c=chr(97+b)
    #print(c)
    r+=c
print(r)


    
#decryption 
d=""
x=input("Enter your code ")
for char in x:

    a=(ord(char)-97)%26
    #print("a",a)
    b=int(0)
    if(a>=shift):
        b=b+(a-shift)%26
    else:
        reminder=a%shift
        b=26-reminder

    c=chr(97+b)
    #print(c)
    d+=c
print(d)