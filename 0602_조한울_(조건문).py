#계산기 프로그램
#조건문
#if 조건 :
#elif조건:
#else :
'''
a=float(input("a를 입력하세요:")) #input ()는 문자열을 입력 받는다
b=float(input("b를 입력하세요:"))
op=input("연산자를 입력하세요:")
if op=='+':
    c=a+b
    print(f"a+b={c}")
elif op=="-":
        c=a-b
        print(f"a-b={c}")
elif op=="*":
    c=a*b
    print(f"a*b={c}")
elif op=="//":
          c=a/b
          print(f"a//b={c}")
else:
    print("연산자 오류")
'''
'''
#음양수 판별 프로그램
c=int(input("숫자를 입력하세요:"))
if c<0:
    print("음수")
elif c>0:
    print("양수")
else:
    print("0")
'''
      
#117pg
#반복문 복습
'''
money=3600
card=True
if money>=3600 and card:
    print("택시타고 가라")
else:
    print("걸어가라")
'''
#성적관리 프로그램
# A :100~91
# B :90~81
# C :80~71
# D :70~61
# F :60~0
# 입력 : 점수
# 출력: 등급
'''
score=int(input("점수를 입력하세요:"))
if 100>=score and 91<=score:
    grade="A"
elif 90>=score and 81<=score:
    grade="B"
elif 80>=score and 71<=score:
    grade="C"
elif 70>=score and 61<=score:
    grade="D"
elif 60>=score and 0<=score:
    grade="F"
print (f'점수는 {score}, 등급={grade}')

if grade=="F":
    print("재수강 하세요")
else :
    print("잘했어요")
'''
import random # random 패키지 사용
num=int(input("숫자를 입력하세요:"))
f=random.randrange(1,11) # 1이상 10 미만의 숫자를 랜덤 생성
if f==num:
        print("정답")
else:
    print("오답")
print(f"정답 {f}입니다")
