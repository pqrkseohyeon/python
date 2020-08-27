# f = open("fruits.txt",encoding='utf-8') # 기본이 ms949
# print(f.read()) # 커서가 맨끝을 가리킴
# print(f.read()) # 읽을 내용이 없음
# content = f.read() # 변수에 저장
# f.close() # 파일을 닫아줌
# print(content)
# print(content)

# 자동으로 파일 닫는 with open 파일 읽기
# with open("fruits.txt", encoding='utf-8') as f:
#     content = f.read()
# print(content)

# 파일 쓰기 (없으면 생성한다.)
# with open("vegi.txt",'w', encoding='utf-8') as f:
#     f.write('무\n')
#     f.write('배추\n')
#     f.write('토마토\n')
#     f.write('브로콜리\n')

# 덧 붙여 쓰기 a
# with open("vegi.txt",'a', encoding='utf-8') as f:
#     f.write('무\n')
#     f.write('배추\n')
#     f.write('토마토\n')
#     f.write('브로콜리\n')

# 파일쓰기, 읽기, 덧붙이기 전부다
# with open("vegi.txt",'a+', encoding='utf-8') as f:
#     f.write('붙여쓰기\n') # 커서가 맨 아래쪽에 있음(공백만 읽었기 때문에 읽을 내용이 없다. 
#                           # (커서를 이동시켜줘야한다.)
#     f.seek(0)           # 커서를 0번째 줄로 이동
#     content = f.read()
# print(content)

# 예제) fruits.txt 파일을 읽고, vegi.txt 파일을 읽고,
#       새 파일 fruitVegi.txt 파일을 만들어 읽어온 fruits와 vegi 파일의 내용을 순서대로 
#       적고 동시에 터미널에 적은 내용을 출력하라.

with open("fruits.txt", encoding='utf-8') as f1:
    content1 = f1.read()

with open("vegi.txt", encoding='utf-8') as f2:
    content2 = f2.read()
with open("fruitVegi.txt","a+", encoding='utf-8') as f3:
    f3.write(content1)
    f3.write(content2)
    f3.seek(0)
    content3 = f3.read()
print(content3)

