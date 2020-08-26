# 내장 함수
# dir() 객체가 가진 메소드를 보여준다.
# print(dir('1'))

# len()
# print(len([1,2,3]))
# print(len("1234"))

# max() min()
# print(max([1,2,3]))
# print(max("한글이다"))

# sum() : 총 합계
# A = [70,60,50]
# print(sum(A))
# print(sum(A)/len(A)) # 평균값 바로 출력 

# 함수 만들기
# def hello():
#   print('하이!')
#   print('안녕!')
#   print('니 하오!')

# hello()
# hello()
# hello()

# 매개변수가 있는 함수
# def hello(name):
#   print('하이 '+name)

# hello('길동')
# hello('펭수')

# 매개변수와 리턴값이 있는 함수
# print(len("문자열 길이"))

# def hello(name):
#   print('하이 '+name)
#   return len(name)

# print(hello("길동"))

# 예제1) 숫자를 입력받아서 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
# def is_odd(n):
#   if n % 2 == 0:
#     return "짝수"
#   else:
#     return "홀수"
# print(is_odd(1))
# print(is_odd(2))

# # 예제2) 입력으로 들어오는 모든 수의 평균 값을 계산해 리턴하는 함수를 작성해 보자.(단 입력으로 들어오는 수의 개수는 정해져 있지 않다.=> 매개변수 앞에 * 붙인다.) ex) def foo(*arg):=>arg 매개변수는 가변갯수 sum()=> 합계
# def avgNums(*num):
#   return sum(num)/len(num)

# print(avgNums(1,2,3))
# print(avgNums(1,2,3,4,5,6,7,8,9,10))
  
# 전역변수와 지역변수
# x = 10 # 전역변수
# def foo():
#   print(x)

# foo()
# print(x)

# # 지역변수 y
# def foo1():
#   y=10
#   print(y)

# foo1()
# #print(y)

# def spam():
#   eggs = 99
#   bacon()
#   print(eggs)

# def bacon():
#   ham = 101
#   eggs = 0

# spam()

# 에러처리 try/Exception

# 어떤 에러인지 알고 있을때.
# def div10(num):
#   try:
#     return 10/num
#   except:
#     print("에러발생")

# print(div10(2))
# print(div10(0)) # 에러발생
# print(div10(5))

# 랜덤 숫자 만들기
# import random

# # 랜덤숫자 = random.randint(1,20)

# for i in range(100):
#   랜덤숫자 = random.randint(1,20)
#   print(랜덤숫자)
#  print(i))

# 숫자 맞추기 게임
# name=(input("당신의 이름은?"))
# print('안녕하세요 {}님 , 1에서 20까지 숫자중 하나를 생각합니다. 맞춰보세요'.format(name))

# import random

# answer= random.randint(1,20)
# print("정답은"+str(answer)+"입니다.")
# count = 6
# i=0

# while i<count:

#   user = int(input("기회가 %d번 남았습니다. 1~20 사이 숫자 입력>> "%(count-i)))
#   i=i+1
#   print("입력한 숫자는 "+str(user)+"입니다.")
  

  
#   if user > answer:
#     print("그 숫자보다 작은수 맞춰보세요")
    
#   if user < answer:
#     print("그 숫자보다 큰수 맞춰보세요.")
#     count
#   if i==count:
#     print("틀렸네요. 정답은 %d입니다."%answer)
#   if user == answer:
#     print("잘 맞췄어요 {}님 %d번만에 숫자를 맞추셨습니다.".format(name)%i)
#     break









