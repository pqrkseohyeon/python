# name = 'Blice'
# if name == 'Alice':
#   print('반가워요 '+name)
# print('종료')

# if else 조건이 맞으면 if문 실행 틀리면 else문 실행
# if문의 실행코드는 들여쓰기가 된 곳 까지이다.
# name = 'Alice'
# if name == 'Alice':
#   print('반가워요 '+name)
#   print('반가워요 '+name)
#   print('반가워요 '+name)
#   print('반가워요 '+name)
#   print('반가워요 '+name)
# else:
#   print('누구신가요?')
#   print('누구신가요?')
#   print('누구신가요?')
#   print('누구신가요?')
#   print('누구신가요?')
#   print('종료')

  # 예제
# name=input("이름을 입력하세요?")

# if bool(name):
#     print(f"당신의 이름은 {name} 입니다.")
# else:
#     print("이름을 입력하지 않았군요!") 
# print("종료")

# while 반복문
# count = 0
# while count<3: # count가 3보다 작을때 계속 반복된다.
#   print('횟수: ',count)
#   count += 1 # 1씩 증가


# treeHit = 0
# while treeHit < 10 :
#   treeHit +=1
#   print(f"나무를{treeHit}번 찍습니다.")
#   if treeHit == 10 :
#     print("나무가 넘어갑니다.")

# 컨티뉴 브레이크
# count=0
# while count < 10 :
#   count += 1
#   if count < 4:
#     continue
#   if count == 8:
#     break
# print(count)

# coffee.py 자판기 코드
# coffee = 10
# while True:
#   money = int(input("돈을 넣어 주세요: "))
#   if money == 300:
#     print("커피를 줍니다.")
#     coffee = coffee -1
#   elif money > 300:
#     print("거스름돈 %d를 주고 커피를 줍니다." %(money -300))
#     coffee = coffee -1
#   else:
#     print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#     print("남은 커피의 양은 %d개 입니다. " %coffee)
#   if coffee == 0:
#     print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#     break

# for 반복문
# for num in [1,2,3]:
#   print(num)

# for ch in '홍길동':
#   print(ch)

# animals = ["개","고양이","스컹크","아나콘다","코끼리","하이에나"]
# for animal in animals:
#   print(animal)

# # range() 
# # (숫자) 0~숫자 -1까지
# for n in range(6):
#   print(n)

#구구단 2단 출력
# for i in range(1,10):
#   print('{}X{}={}'.format(2,i,2*i),end=" ")

# 구구단 2단~9단까지 출력
# for i in range(2,10):
#   print() # 한줄 띄움
#   for y in range(1,10):
#     print('{}X{}={}'.format(i,y,i*y),end=" ")

# 예제1) 다음코드의 실행 결과는?

# a = "Life is too short, you need python"

# if "wife" in a: # a에 wife가 있으면 T 없으면 F
#   print("wife")
# elif "python" in a and "you" not in a : #a에 python이 있고 you가 없어야 T 하나라도 만족 못 하면 F 
#   print("python")
# elif "shirt" not in a: # a에 shirt가 없으면 T 
#   print("shirt")
# elif "need" in a:
#   print("need")
# else:
#   print("none")

# print("----------------------")
# # 예제2) while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자
# i=1
# count=0
# while i<= 1000: # 1~1000
#   if i%3==0: # 3의 배수
#     count=count+i
#   i= i+1
# print(count)

# print("----------------------")
# # 예제3) while문과 for문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성
# for a in range(1,6):
#   for b in range(a):
#     print("*",end=" ")
#   print()

# for i in range(6):
#   print('*'*i) # i의 값에 따라 별이 찍힘

# print("----------------------")
# # 예제4) A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다. [70,60,55,75,98,90,80,80,85,100] for문을 사용하여 A학급의 평균 점수를 구해보자
# A = [70,60,55,75,95,90,80,80,85,100]
# total=0
# for i in A:
#   total += i
# avg=total/len(A)
# print(avg)

# print("----------------------")
# # 컴프리헨션
# list_num = [1,2,3,4,5,6,7,8,9,10]
# 홀수 = []

# for num in list_num:
#   if num % 2 ==1:
#     홀수.append(num)

# print(홀수)

# 홀수 = [num for num in list_num if num%2 == 1]

# 리뷰 문제 풀어보기
print("-------------------------------")
# 001 문자열 출력하기
print("Hello World")

print("-------------------------------")
# 002  print 출력하기
x = 1000
y = "일이삼사오"
z = 1.2345

print(x,y,z)

print("-------------------------------")
# 003 문자열 출력하기
print("신씨가 소리질렀다.\"도둑이야\".") 

print("-------------------------------")
# 004 탭과 줄바꿈
print("안녕하세요.\n만나서\t반갑습니다.")

print("-------------------------------")
# 005 포맷 연산자
x,y =10,3
print("%.3f"%(x/y))

print("-------------------------------")
# 006 사용자 입력
x=int(input("정수입력1 : "))
y=int(input("정수입력2 : "))
print('합은 : {} 입니다.'.format(x+y))

print("-------------------------------")
# 007 사용자 입력
# a=input("문자열 : ")
a=input("문자열 : ")
b=int(input("반복횟수 : "))
for i in range(b):
    print(a ,end=' ')

print("-------------------------------")
# 008 사칙연산
f_num=int(input("first number : "))
s_num=int(input("second number : "))
print('add :{}'.format(f_num+s_num))
print('sub :{}'.format(f_num-s_num))
print('mul :{}'.format(f_num*s_num))
print('div :{}'.format(f_num/s_num))

print("-------------------------------")
# 009 파이써너 계산하기
a = 48584
tot = a*36
print('총 금액은 {}원'.format(tot))

print("-------------------------------")
# 010 format 함수
name=str(input("이름?"))
color=str(input("컬러?"))
print('안녕하세요. 제 이름은 {}이고, 좋아하는 색상은 {} 입니다.'.format(name,color))