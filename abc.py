a,b,c=int(input()),int(input()),int(input())
h=0
if a>b and a>c:
    print(f'{a}is the greates among{a,b,c}')
    h=a
elif b>a and b>c:
    print(f'{b}is the greates among{a,b,c}')
    h=b
else:    
    print(f'{c}is the greates among{a,b,c}')
    h=c

x,y=1,1
print(x)
for i in range(h-1):
    print(y)
    x,y=y,x+y