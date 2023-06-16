list1=["abd","dfg","hij",123,456]
list1[1]="park"
'''
list2=[4,8,12,16,20,24,28,32]
arr=list2
print(f'{arr}')
'''
'''
arr=[4,8,12,16,20,24,28,32]
arr1=[]
a=1
while True:
    if a==9: break
    arr1.append(4*a)
    a=a+1
print(arr1)
'''
'''
arr=[12,13,56,14,4,77,15,96]
size=len(arr) # 리스트이 크기 변수
print(size)

idx=0
while True:
    idx1=idx+1
    if idx1==size:break
    if arr[idx]>arr[idx1]:
           tmp=arr[idx]
           arr[idx]=arr[idx1]
           arr[idx1]=tmp
    idx=idx+1
    print(arr)
print("------------------------------------------")
print(sorted(arr))
print(list(reversed(arr)))
'''
#내 생일 요일 찾기
'''
import datetime
today=datetime.datetime.now()
if today.weekday() ==6 or today.weekday()==5:
    print("주말")
else:
    print("평일")
print("내가 태어난날의 요일 맞추기")
y = int(input("년입력:"))
m = int(input("월입력:"))
d = int(input("일입력:"))

date=datetime.datetime(y,m,d)
if date.weekday()==0: print("월")
elif date.weekday()==1: print("화")
elif date.weekday()==2: print("수")
elif date.weekday()==3: print("목")
elif date.weekday()==4: print("금")
elif date.weekday()==5: print("토")
elif date.weekday()==6: print("일")
'''
import random
# 컴퓨터
while True:
    com=random.choice("RSP")
    user=input("R,S,P 중 하나를 고르세요:")

    if user==com:
        print("비김")
    elif (com=="R" and user=="P") or (com=="S" and user=="R") or (com=="P" and user=="S"):
        print("이김")
        break
    elif (user=="R" and com=="P")or (user=="S" and com=="R")or (user=="P" and com=="S"):
        print("짐")

    print(f'컴퓨터 : {com},인간: {user}')

