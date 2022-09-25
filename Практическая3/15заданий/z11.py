x= int(input("Введите x: "))
y = int(input("Введите y: "))
if x==4 and y<2:
    q=x+x*y
elif x<y:
    q=y*y+1
else: 
   q=y*y+4
print("q= ",q)