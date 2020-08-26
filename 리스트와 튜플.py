# 리스트 [ , , ] - 리스트는 대괄호 사이에 아이템들이 들어간다.
# spam = ['개','고양이','박쥐','곰']
# print(spam)
# print(spam[0]) # 개
# print(spam[1]) # 고양이
# print(spam[2]) # 박쥐
# print(spam[3]) # 곰
# #print(spam[4]) # 인덱스 범위를 초과 (없는 인덱스 번호를 넣으면 오류가 난다.)

# # 이중 리스트
# ham = [ ['고양이','강아지'],[10,20,30,40,50] ]
# print(ham)
# print(ham[0])
# print(ham[1])
# print(ham[0][0])
# print(ham[0][1]) # 강아지
# print(ham[0][1][2]) # 강아지 - 글자 슬라이싱 해서 2번째 글자인 '지'가 출력된다.

# # 인덱스 번호가 음수일때 - 뒤에서부터 시작한다. 
# print(spam[-1])
# print(spam[-2])
# print(spam[-3])
# print(spam[-4])

# 슬라이싱 [시작위치:마지막위치-1]
# print(spam[0:2]) # 0 1 -> 개, 고양이
# print(spam[2:])  # 2번째부터 끝까지 - 마지막위치를 지정안하면 끝까지이다.  

# # 예제 리스트 만들기
# # 숫자, 소수, 문자열이 있는 myList
# myList = [1, 3.14, "문자열"]
# print(myList)
# print(myList[1])

# 튜플(Tuple) ( , ,)
# 리스트와 비슷
# 값을 변경불가 순서 있음

# list1 = [ 1, 2, 3]
# list1[0] = 9 # 리스트는 값을 변경가능
# print(list1)

# tuple1=(1,2,3)
# # tuple1[0] = 9 # 에러발생 - 튜플은 값 변경 불가능
# print(tuple1[2]) 

# # 튜플은 값 변경 불가이며 그외에는
# # 리스트와 비슷하다.
# # 슬라이싱, 인덱싱,

# # 더하기와 곱하기
#   # 더하기
# list2 = list1 + list1
# print(list2)
# tuple2 = tuple1 + tuple1
# print(tuple2)
#   # 곱하기
# list3 = list1 * 3
# print(list3)
# tuple3 = tuple1 * 3
# print(tuple3)

# # 길이 구하기
# print(len(list3))
# print(len(tuple3))

# 리스트의 메소드
#list1 = ['개','고양이','박쥐','곰']

# 추가 append()
# list1.append('염소')
# print(list1)

# 빼기 pop() - 맨 뒤의 아이템 제거
# list1.pop() # 기본 인덱스 번호가 -1 
# print(list1)
# list1.pop(0) # 인덱스 번호 지정 가능하다.
# print(list1)

# 리스트에 요소입력 insert()
# insert(index, 아이템)
# list1.insert(1,'사람')

# # 아이템의 값으로 제거
# # remove(아이템)
# list1.remove('고양이')

# # index() 인덱스 번호를 확인
# # index(아이템)

# print(list1.index('사람'))

# 리스트의 정렬 sort()
list1 = [5,9,1,7]
list1.sort() # 정렬함
print(list1)
# 반대로 정렬
list1.sort(reverse=True) 
print(list1)