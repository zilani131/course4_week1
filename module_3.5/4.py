z=input()
up=int(0)
low=int(0)
di=int(0)
sy=int(0)
for i in z:
    if(ord(i)>=ord('a')and ord(i)<=ord('z')):
        low=low+1
    elif(ord(i)>=ord('A')and ord(i)<=ord('Z')):
        up=up+1
    elif(ord(i)>=ord('0')and ord(i)<=ord('9')):
        di=di+1
    else:
        sy=sy+1
print(f'Upper : {up}',f'lower : {low}',f'Digit : {di}',f'symbol : {sy}')