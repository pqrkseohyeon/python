# 001 함수만들기
# 함수 add는 매개변수로 a와 b를 받고 있습니다. 코드의 3번째 줄을 수정해서 result에 a와 b를 더한 값을 저장하고 출력되도록 만들어 보세요.

def add(a,b):
  result=a+b
  print("{} + {} = {}".format(a,b,result))
add(10,5)

# #002 함수의 리턴
# # 매개변수로 변수 a와 b를 받는 함수 add를 정의하고 a와 b를 더한 값을 return해 보세요.
def add(a,b):
  return a + b
print(add(10,5))

# 003 List 리스트
# 리스트는 여러개의 값을 담을 수 있는 변수입니다.
# 리스트 rainbow의 첫번째 값을 이용해서 무지개의 첫번째 색을 출력하는 코드입니다. first_color에 무지개의 첫번째 값을 저장하도록 수정해 보세요.
rainbow=['빨강','주황','노랑','초록','파랑','남색','보라']

first_color = rainbow[0]
print('무지개의 첫번째 색은 {}이다'.format(first_color))

# 004 리스트 사용하기
# 리스트 rainbow의 마지막 값을 이용해서 무지개의 마지막 색을 출력하는 코드입니다. last_color에 rainbow의 마지막 값을 저장하도록 수정해보세요.
rainbow=['빨강','주황','노랑','초록','파랑','남색','보라']

last_color = rainbow[-1]
print('무지개의 마지막 색은 {}이다.'.format(last_color))

# 005 리스트 추가하기
# append를 이용해 보세요.

list1=[1,2,3]
list1.append(4)
print(list1)

list = [1,2,3]
list += [4]
print(list)

# 006 리스트 수정
# 리스트에 값이 들어있는지 확인하려면 in 연산을 이용하면 됩니다.
# numbers에 5가 들어있을때, 5가 있다를 출력하도록 빈칸을 채워보세요.
numbers = [1,2,3,4,5]
n = 5
if n in numbers:
  print('{}가 리스트에 있다.'.format(n))

# 007 리스트 지우기
# list1에 포함된 2를 지워서 list1의 값이 [1,3]이 되도록 만들어보세요.
list1 = [1,2,3]
list1.remove(2)
print(list1)

# 008 딕셔너리 만들기
# 딕셔너리란 여러 값을 저장해 두고 필요한 값을 꺼내 쓰는 기능입니다.
# 이름표를 이용하여 값을 꺼내 사용하며, 리스트와 비슷한 방식을 갖습니다.
# 문제 : 월을 이름표로 가지고, 그 달에 있는 날짜 수를 값으로 가지는 딕셔너리를 만들어서 days_in_month에 저장해 보세요. 월은 '1월','2월'과 같은 형식으로 저장하면 됩니다. 

days_in_month = {
  '1월':'31일',
  '2월':'28일',
  '3월':'31일'
}
print(days_in_month)

# 009 딕셔너리 입력 자료형
# 딕셔너리의 이름표(key)는 문자열과 숫자형, 튜플을 사용할 수 있으며, 값(value)으로는 어떤 자료형이 오던 상관 없습니다.
dict = {
  '이름':'홍길동',
  '번호':'1010',
  '취미':'["낮잠","숨쉬기","커피"]'
}
print(dict)

#010 딕셔너리 수정하기
# days_in_month에는 2월이 28일까지 있다고 만들어져 있는데요.
# 알고보니 2016년에는 2월이 29일까지 있습니다.
# 2월이라는 이름표가 가지는 값을 29로 수정해 보세요.
days_in_month = {
  '1월':'31일',
  '2월':'28일',
  '3월':'31일'
}
days_in_month["2월"]="29일"

print(days_in_month)

# 011 딕셔너리 삭제하기
# days_in_month에는 엉뚱하게도 -1월이라는 이름표와 값이 있는데요.
# 이 값을 지워보세요.
days_in_month = {"1월":31,"2월":28,"3월":31,"-1월":97889789}
del days_in_month['-1월']
print(days_in_month)

# 012 딕셔너리와 반복문
# for in문을 이용해서 days_in_month의 이름표(key)를 한줄씩 출력해 보세요.
days_in_month = {"1월":31,"2월":28,"3월":31,"4월":30,"5월":31}
for k in days_in_month.keys():
  print(k)

# 013 문자열 출력
days_in_month = {"1월":31,"2월":28,"3월":31,"4월":30,"5월":31}

for k,v in days_in_month.items():
  print('{}은 {}일이 있습니다.'.format(k,v))

# 014 random 실습
# random.choice를 활용하여 random_element가 list의 element중 하나를 가지도록 만들어 보세요.
import random
list = ["빨","주","노","초","파","남","보"]
random_element = random.choice(list)
print(random_element)

# 015 random 실습
# random.randint를 활용하여, randow_number가 2보다 크거나 같고, 5보다 작거나 같은 임의의 정수를  가지도록 만들어라
import random
random_number= random.randint(2,5)

print(random_number)

# 016 문자열 출력하기
# random.shuffle 활용
# random.shuffle()을 활용해서 list의 순서를 섞어 보세요.

import random
list = ["빨","주","노","초","파","남","보"]
random.shuffle(list)
print(list)

# 017 datetime 실습
# datetime 활용해서 오늘날짜 출력
import datetime
print(datetime.date.today())

# 018 문자열 실습
# 다음과 같은 문자열을 값으로 가지는 변수 string1을 선언하세요.
string1 = '''
다스베이더가 말했다.
"내가 니 애비다!"
그 말을 들은 루크는 '깜짝' 놀랐다.
'''

list1=string1.split()
print(list1[4])

# 019 반복문 사용하기
# days에는 1월부터 12월까지 그 달에 포함된 날짜수가 정리되어 있습니다.
# 다음과 같이 출력되도록 for in문을 만들오 보세요.
days = [31,29,31,30,31,30,31,31,30,31,30,31]

for idx, val in enumerate(days):
 
  print('{}월의 날짜수는 {}일 입니다. '.format(idx+1,val))

# 020 정수와 실수 
# 변수 div를 선언하고, 변수 a를 b로 나눈 몫을 값으로 가지도록 계산해 보세요.
a = 23
b = 5
div = int(a/b)
print("a를 b로 나눈 몫은 {}입니다.".format(div))

# 21 while문 실습
# length 변수를 이용해서 한 줄씩 출력
numbers = [1,2,3]
length = len(numbers)
i = 0
while length>i:
  print(numbers[i])
  i = i+1

# 022 enumerate
# 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가집니다.
# 이 함수는 순서가 있는 자료형(list,set,tuple,dictionary,string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.

sizes = [33,35,34,37,32,35,39,32,35,29]
for i, size in enumerate(sizes):
  if size == 32:
    print("사이즈 32인 바지는 {}번째에 있다.".format(i+1))
    break

# 023 예외 try except
# 다음 코드는 3을 0으로 나누고 있습니다.
# 나눗셈 연산은 0으로 나눌 수 엇기 때문에 문제의 코드를 실행하면 에러가 발생합니다. 에러의 이름을 확인하고 try except문으로 줄을 감싸서 에러가 발생할 경우 print문이 출력되도록 만들어 보세요.
try:
  a=3/0
except Exception:
   print("0으로 나눌 수 없습니다.")


# 024 예외의 이름을 알고싶을때
# 예외의 이름을 모르는 경우에는 Exception as를 통해 해결할 수 있습니다.
# 어떤 에러가 발생하는지 출력할 수 있도록 빈칸을 채우고, 예외를 출력할 수 있도록 format의 빈칸을 작성하세요

try:
  a=5
  b=0
  c=a/b
except Exception as ex:
  print("다음과 같은 에러가 발생했습니다: {}".format(ex))

# 025 딕셔너리 중복
# 다음 코드는 문구점 3곳을 검사하면서 풀이 있으면 문구점의 이름과 가격을 출력합니다.
shops = {
  "송일문방구":{"가위":500,"크레파스":3000},
  "알파문구":{"풀":800,"도화지":300,"A4용지":8000},
  "다이소":{"풀":500,"목공본드":2000,"화분":3000}
}

for shop, products in shops.items():
  for product, price in products.items():
    if product=='풀':
      print("{}: {}원".format(shop,price))

# 026 bool 논리 연산
# 다음중 어떤 if코드가 실행되는지 확인하시오.
if []:
  print("[]은 True입니다.")

if [1,2,3]:
  print("[1,2,3]은/는 True입니다.")

if{}:
  print("{}은 True입니다.")

if{'abc':1}:
  print("{'abc':1}은 True입니다.")

if 0:
  print("0은/는 True입니다.")

if 1:
  print("1은 True입니다.")


# 027 논리연산자 or
# or 연산의 결과는 앞의 값이 True이면 앞의 값을,
# 앞의 값이 False이면 뒤의 값을 따릅니다.
# 다음 코드를 실행해서 각각 a와 b에 어떤 값이 들어가는지 확인해 보세요.

a = 1 or 10 # 1의 bool 값은 True입니다.
b = 0 or 10 # 10의 bool 값은 False입니다.

print("a:{}, b:{}".format(a,b))

# 028 리스트 실습
# list1의 1번째 자리에 8을 넣고 원래 있던 값은 오른쪽으로밀어 보세요.
list1 = [1,2,3,4]
list1.insert(1,8)
print("첫 번째 자리에 8을 넣은 결과 : {}".format(list1))

# list1을 작은 수부터 큰 수로 정렬해 보세요
list1.sort()
print("list1을 작은 수부터 큰 수로 정렬한 결과 : {}".format(list1))

# 아래줄에서 list1을 거꾸로 만들어 보세요
list1.reverse()
print("list1을 거꾸로 정렬한 결과 : {}".format(list1))

# 029 문자열과 리스트
str ="10:35:27"
list = str.split(":")
new_str=":".join(list)
print(list)
print(new_str)

str = "오늘은 날씨가 흐림"
# split()을 이용해서 str을 공백으로나눈 문자열을 words에 저장해세요
words = str.split()

# index()를 이용해서 "흐림"이 words의 몇번째에 있는지 찾고, 
# position에 저장해세요
position = words.index('흐림')

words[position] = "맑음" # 흐림을 맑음으로 수정

# join()을 이용해서 words를 다시 문자열로 바꿔 new_str에 저장하세요.
# words를 문자열로 바꿀때는 공백 한 칸을 기준으로 붙이면 됩니다.
new_str="".join(words)
print(new_str)

# 030 리스트 slice 
# slicing - 리스트나 문자열에서 여러개의 값을 가져오는 기능입니다.
rainbow = ["빨","주","노","초","파","남","보"] 
# red_colors가 ["빨","주","노"]의 값을 가지도록 rainbow를 slice 하세요
red_colors = rainbow[0:3]
# blue_colors가 ["파","남","보"]의 값을 가지도록 rainbow를 slice하세요
blue_colors = rainbow[4:]
print("red_colors의 값 : {}".format(red_colors))
print("blue_colors의 값 : {}".format(blue_colors))

