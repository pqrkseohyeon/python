# 문자열 메소드
# 대 소문자
# string1 = 'Hello World'
# print(string1.upper()) # 대문자
# print(string1.lower()) # 소문자
# print(string1)

# print("title title".title()) # 단어의 첫 글자를 대문자로 바꿔서 리턴

# # 문자열 개수 세기 count()
# print(string1.count('o'))
# print(string1.count('Hello'))

# string2 = "안촉촉한 초코칩나라에 살던 안촉촉한 초코칩이 촉촉한 초코칩나라의 촉촉한 초코칩을 보고 촉촉한 초코칩이 되고싶어서 촉촉한 초코칩나라에 갔는데 촉촉한 초코칩나라의 문지기가 "
# print(string2.count('촉'))

# 알파벳, 숫자, 공백 인지 확인
# print('hello'.isalpha()) # hello가 앒파벳인가 -> True
# print('hello123'.isalpha()) # hello123이 알파벳인가 -> False
# print('hello123'.isalnum()) # 알파벳+숫자 -> True
# print('123'.isdecimal()) # 숫자인가 -> True
# print(' '.isspace()) # 문자열 공백인가 -> True 

# 문자열의 시작과 끝을 체크
# print('hello'.startswith('h'))
# print('hello'.startswith('H'))
# print('hello'.endswith('o'))

# 문자열 삽입 join
# print('!'.join('abcd')) # 각각의 문자에 , 가 들어가서 출력된다.
# # 리스트를 문자열로 만듬
# print('=='.join(['1','2','3']))

# print('-'.join(['2020','05','20']))

# 문자열 나누기 split()
print("2020-05-20".split('-'))
print("2020 05 20".split()) #공백으로 나누어진다.

# 공백제거(입력을 받을때)
print('    하이    ')
print('    하이    '.strip())

# 문자열 바꾸기 replace
a = "인생은 짧다."
print(a.replace("인생은", "하루가"))


