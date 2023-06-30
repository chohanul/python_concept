#구구단 9단 출력
'''
for j in range(1,101,1):
    for i in range(1,101,1):
        mul=j*i
        print(f'{j}*{i} = {mul}')
    print("----------------------")
'''
#1부터 100까지 홀수만 출력
#case 1
'''
for i in range(1,101,2):
    print(i)

#case 2
for o in range(1,101,1):
    if o%2==1:
        print(o)
'''
'''
for i in range(5,101,5):
    print(i)
    
for o in range(1,101,1):
    if o%5==0:
        print(o)

for i in range(1,101,1):
    print(i*i)

for o in range(1,101,1):
    print(o**2)

for p in range (1,101,1):
    print(p**3)
    '''
'''
a= "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
'''
'''
result = 0
i=1
while i<= 1000:
    if i%3==0:
        result=result+i
    i=i+1
print(result)
'''
result=0
for i in range(1,1001,1):
    if i%3==0:
        result+=i
        i+=1
print(result)
    
    
