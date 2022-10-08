from unittest import result


data="Nea/caiuoeTA"
new_data=data.lower()
result=''
for cha in new_data:
    if(cha=='a'or cha=='e'or cha=='i'or cha=='o'or cha=='u'):
        result+=cha+" "

print(result)