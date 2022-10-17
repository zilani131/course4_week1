from ctypes.wintypes import CHAR
from lib2to3.pgen2.token import STRING
from tokenize import String


z=input()
c=""
for i in z:
    if ord(i)>=ord('a')and ord(i)<=ord('z'):
        c=c+chr(ord('A')+ord(i)-ord('a'))
    elif  ord(i)>=ord('A')and ord(i)<=ord('Z'):
         c=c+chr(ord('a')+ord(i)-ord('A'))
    else:
        c=c+i

print(c)