# 기본 테이터 타입
int # 정수
float # 실수
bool # 불린(참,거짓)
str # 문자
list 
tuple
dict

# None : null과 비슷
None


# 숫자( int  float) : 정수, 실수
# type() : 자료형 리턴
# print(type(2+4))
# print(type(2-4))
# print(type(2*4))
# print(type(2/4))


# print(type(0.00001))
# print(type(5.00001))
# print(type(0.0))
# print(type(0))

# print(type(9.9+1.1))

# 제곱과 나누기
# 거듭제곱 **
# print(2**4)
# # 나누기 몫 // 
# print(10//4)
# # 나누기 나머지 %
# print(10%3)

# # Math 수학 함수
# # 반올림 round(숫자, 자릿수)
# print(round(3.123456, 3))
# # 절대값 abs
# print(abs(-20))

# 숫자 계산시 우선순위
# print((20-3)+2**2)


# 1. ()
# 2. **
# 3. * /
# 4. + -

# 이진수 변환 bin()
# print(bin(5))
# print(int('0b101',2))

# 변수
# iq = 190 # 메모리에 숫자 190은 바이너리(2진수)로 저장됨
# print(iq)

# 여러개의 변수를 초기화
# a,b,c =1,2,3
# print(a)
# print(b)
# print(c)

# 예제 1
# 틀린 변수 이름을 찾고 잘못된 변수 이름은 바르게 고쳐주세요

# 놀이기구 = "자이로드롭"
# a,b,c,d = 1,2,3,4
# 이름 = "박써니"
# _myName = "홍길동"

# # 예제2
# # print() 출력 함수를 이용하여 x변수에 값 10을 저장하고 출력
# x=10
# print(x)

# # 예제3
# # 여러개의 변수 x,y,z에 각각 1,2,3 을 저장하고 출력하라
# x,y,z=1,2,3
# print(x)
# print(y)
# print(z)

# # 예제4 
# # 결과가 <class 'int'> <class 'float'> <class 'str'> 같이 나오도록 x,y,z 값에 정수, 소수, 문자열을 입력하여 그 타입(Type)을 출력
# x,y,z=1,2.2,"문자"
# print(type(x))
# print(type(y))
# print(type(z))

# 문자형 데이터 str
# 쌍따옴표, 한따옴표 
# print(type('문자열'))
# var1 = '한따옴표'
# var2 = "쌍따옴표"
# print("문자열은 "+var1+var2)
# print("문자열은",var1,var2)
# # 따옴표가 3개씩 쓸때 '''  """
# var3 = '''
# 따옴표 3개는
# 문장 모두를
# 처리하는 문자열
# --------------
# '''
# print(var3)
# # 문자열(+)연산
# 성 = '홍'
# 이름 = "길동"
# name = 성 + ' ' + 이름
# print(name)

# 타입 변환 str(),int(),float()
# num = input("숫자 하나 입력:")
# print(int(num)+10) # num은 문자로 인식되기 때문에 숫자로 형변환해서 입력해야지 에러가 안난다.

# 이스케이프 시퀀스
# \가 있으면 뒤에 문자라고 인식한다.
# 날씨 = "It\'s \"kind of\" sunny"
# print(날씨)

# 예제1
#아래와 같이 출력 되도록 변수 날씨에 이스케이프 문자들을 추가하여 만들어라.
# 날씨2 = "\tIt\'s \"kind of\" sunny\n Have a nice Day!"
# print(날씨2)

# # 예제2
# # 다음과 같은 문단을 문자열을 값으로 가지는 변수 string1을 선언하세요.
# string1='''
# 다스베이더가 말했다.
# "내가 니 애비다!"
# 그 말을 들은 루크는 '깜짝' 놀랐다.
# '''
# print(string1)

# f-string 문자열 포맷
# name="홍길동"
# age=20 #정수

# # print('안녕하세요 '+name+"님 나이가 "+str(age)+"이군요")
# print(f'안녕하세요 {name}님 나이가 {age}살 이군요')
# # printf 방법
# print("나는 도시락 %d개를 %s 먹었다." % (7,'배터지게'))

# #문자열.format() 함수 방법
# number = 20
# welcome = "환영합니다."
# base = '{} 번 손님 {}'

# print('{} 번 손님 {}'.format(number,welcome))
# print(base.format(number,welcome))

# #예제1
# name="홍길동"
# color="보라색"
# print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name,color))
# print(f'안녕하세요. 제 이름은 {name}이고 좋아하는 색상은 {color}입니다.')

# 문자열의 인덱스
# string1 = '01234567'
#          01234567 인덱스 번호
# 문자열[인덱스번호]
# print(string1[3])

# 문자열 슬라이싱 [시작:끝-1]
# string1 = '01234567'
# print(string1[1:5]) #1부터 시작해서 5전까지 출력한다.
# print(string1[0:3]) 
# print(string1[:3]) #처음부터
# print(string1[3:]) #끝까지

# # #[시작:끝:증감]
# print(string1[::2])#0부터 시작 2씩 증가 2 4 6
# print(string1[::-1])# 거꾸로 출력
# string2 = 'god'
# print(string2[::-1])

# 슬라이싱 예제
# red_colors가 [빨,주,노]의 값을 가지도록 rainbow를 slice 하세요.
# blue_colors가 [파,남,보]의 값을 가지도록 rainbow를 slice 하세요.
# rainbow=["빨","주","노","초","파","남","보"]
# red_colors=rainbow[0:3]
# blue_colors=rainbow[4:7]

# print("red_colors의 값 :{} ".format(red_colors))
# print("blue_colors의 값 : {}".format(blue_colors))

# 문자열의 변경불가
# 문자열은 부분적으로 변경불가
# # string1 = '123'
# # string1[0] = '9'

# # len(문자열) 문자열의 길이
# print(len("123456"))

# bool 참 거짓 형
# bool1 = True
# bool2 = False
# bool3 = 1 < 2 # T
# bool4 = 1 == 2 # F

# print(bool1)
# print(bool2)
# print(bool3)
# print(bool4)

# x,y=1,2
# print(x > y)
# print(x == y)
# print(x != y)
# # 불린타입 변환 bool() 
# print(bool(1)) # T
# print(bool(0)) # F
# print(bool('True')) # T 문자열은 값이 있으면 true가 된다.
# print(bool('안녕')) # T

# 논리 연산자
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# or
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# not
print(not True)
print(not False)

