#1번
'''
print(3==2)
print(4 !=4)
print(5>=10
'''
#2번
'''
a=int(input("C언어 성적:"))
b=int(input("파이선 성적:"))
c=int(input("자바 성적:"))

sum=a+b+c
avg=sum/3
if avg>=80:
    print("합격")
else:
    print("불합격")
'''
'''
#3번
a=int(input("양의 정수를 입력하세요:"))
if a%3==0 and a%2==0:
    print("3과 2의 배수")
elif a%3==0:
    print("3의배수")
elif a%2==0:
    print("2의배수")
    
else:
    print("2와 3의 배수가 아님")
'''

#4-1번 슷자 만들기 게임

'''import random
ans=random.randrange(0,10) #0 이상 10 미만 숫자 랜덤 생성
c=0 #기회

while True:
    c=c+1
    print("-----------------------")
    me = int(input("숫자 입력:"))
    if ans<me:
        print("down")
        print(f"기회 :{c}")
    elif ans>me:
        print("up")
        print(f"기회 :{c}")
    else:
        print("정답")
        print(f"기회 :{c}")
        break
        '''
'''
while 1:
    num= input("알파벳을 입력하시오(z누르면 종료!)")
    if(num=="z"):
        break
    print(num)
'''


#야구게임
import random
a=random.randrange(1,10) # 1~9숫자 랜덤 생성
b=random.randrange(1,10) # 1~9숫자 랜덤 생성
while a==b:
    b=random.rangrange(1,10)
c=random.randrange(1,10)
while c==a or c==b:
    c=random.randrange(1,10)

com=[a,b,c]
chance=1
while True:
    print(f'{chance}번쨰 도전이다. 숫자 입력')
    s=0
    ball=0

    #사용자 입력
    user_a=int(input("첫번째 수:"))
    user_b=int(input("두번째 수:"))
    user_c=int(input("세번째 수:"))

    chance=chance+1
    if user_a in com:
        if user_a==a:
            s=s+1
        else:
            ball=+1
    if user_b in com:
        if user_b==b:
            s+=1
        else:
                ball+=1
    if user_c in com:
        if user_c==c:
            s=s+1
        else:
                ball=+1
    print(f'스트라이크 :{s}, 볼 :{ball}')
    if s==3:
        break
    
print(f'정답은 {com}입니다. 당신은 {chance-1}만에 맞춤')
                
