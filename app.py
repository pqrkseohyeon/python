import json # json 라이브러리 불러오기
import difflib # 비슷한 단어 찾기

data = json.load(open('data.json')) # 제이슨 파일을 불러옴

def translate(word): #data 안에 있는 단어(key)가 있으면 value를 리턴
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data: # 대문자로만 이루어진 단어검색
        return data[word.upper()]
    elif word.title() in data: # title은  맨앞글자만 대문자로 바꿔준다.
        return data[word.title()]
    else:
        match = difflib.get_close_matches(word,data.keys())
        if len(match) > 0:
            print(f'혹시 입력한 단어가 {match[0]}인가요?')
            answer = input('맞으면 y 아니면 n 입력 :')
            if answer == 'y':
                return data[match[0]]
        return "그런 영어단어는 없습니다. 철자를 체크하세요."
#print(translate('rain'))
word = input("영어단어 입력 : ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)