#2023.05.12
'''
a=int(input('a를 입력하세요:'))
b=int(input('b를 입력하세요:'))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)
'''
'''
a=int(input('a를 입력하세요:'))
b=int(input('b를 입력하세요:'))

print("a=%d 입니다.b=%d입니다"%(a,b))
'''

name="조한울"
age=16
height=165
print("제 이름은 %s입니다.\n 나이는 %d, 키는 %d" %(name,age,height))

hope=int(input("희망하는 키를 작성해라:"))
print("제이름은 %s입니다.나이는 %d, 희망키는 %d" %(name,age,height))
print("제이름은 {}입니다.나이는{}, 희망키는 {}.".format(name,age,hope))

tmp=hope-height

print("그럼 앞으로 %d 만큼 커야겠네요ㅋㄷ"%(hope-height))
print("그럼 앞으로 "+str(tmp)+"만큼 커야겠네요ㅋㄷ")
