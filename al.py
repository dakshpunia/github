a,b,c=int(input()),int(input()),int(input())
if a>b and a>c:
    print(f'{a}is the greates among{a,b,c}')
elif b>a and b>c:
    print(f'{b}is the greates among{a,b,c}')
else:    
    print(f'{c}is the greates among{a,b,c}')

name,age=input('What\'s your name?'),a*b*c
print(f'Hello!{name}, i know you were born in the year{2024-age} and you are a gem of a person. Nice time meeting you, See you soon!!!')
x,y=1,1
print(x)
for i in range(age**0.5):
    print(x,end=', ')
    x,y=y,x+y