# a=int(input("정수1:"))
# b=int(input("정수2:"))
# result=a+b
# print("합은 : {} 입니다.".format(result))

# a=int(input("first number:"))
# b=int(input("second number:"))

# print("add : %d"%(a+b))
# print("sub : %d"%(a-b))
# print("mul : %d"%(a*b))
# print("div : %.1f"%(a/b))

# # 구구단 2단~9단까지 출력
# for i in range(2,10):
#   print() # 한줄 띄움
#   for y in range(1,10):
#     print('{}X{}={}'.format(i,y,i*y),end=" ")


# 숫자 맞추기 게임
# name=(input("당신의 이름은?"))
# print('안녕하세요 {}님 , 1에서 20까지 숫자중 하나를 생각합니다. 맞춰보세요'.format(name))

# import random

# com_num = random.randint(1,20)

# while True:
#   cnt=6
#   i=0
#   player_num=0
#   print("1~20 사이의 숫자를 맞춰보세요")
#   while com_num!=player_num:
#     player_num=int(input("당신이 선택한 숫자는?"))

#     if player_num>com_num:
#       print('더 작은 수 맞춰보세요.')
#     elif player_num<com_num:
#       print("더 큰 수 맞춰보세요.")
#     elif player_num==cnt:
#       print("맞았습니다.")
#     elif cnt >6:
#         print("틀렸습니다. 기회를 모두 소진하였습니다.")
#         break
#         cnt=cnt+1
#     else:
#         print(cnt,"번 만에 맞혔습니다.")

#   q_continue=input("계속하시겠습니까?(y/n)")
#   if q_continue=='n':
#     break

# # 05 정수 (int)의 길이를 구하라.
# def number_length(a:int):
#     return  len(list(str(a)))

# if __name__ == '__main__':
#     print(number_length(10))
#     print(number_length(0))
#     print(number_length(4))
#     print(number_length(44))
    

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert number_length(10) == 2
#     assert number_length(0) == 1
#     assert number_length(4) == 1
#     assert number_length(44) == 2

# # 09 리스트를 입력받아 첫번째  아이템을 맨 마지막으로 보낸 다음 리턴, 빈 리스트 []나 [1] 하나의 값이 있을때는 같은 리스트가 리턴
# def replace_first(items:list):
#     if len(items) > 0:
#         first_list = []
        
#         for i in items[:1]:
#             first_list.append(i)
            
#         return items[1:] + first_list
        
#     else:
#         return items
   

# if __name__ == '__main__':
#     print(list(replace_first([1, 2, 3, 4])))
#     print(list(replace_first([1])))
#     print(list(replace_first([])))
    

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
#     assert list(replace_first([1])) == [1]
#     assert list(replace_first([])) == []

# 04 패스워드는 길이가 6보다 커야 한다. => 크면 True 틀리면 False 리턴
# def is_acceptable_password(password: str):
#     if len(password) > 6:
#         return True
#     else:
#         return False
    
# if __name__ == '__main__':
#     print(is_acceptable_password('short'))
#     print(is_acceptable_password('muchlonger'))
#     print(is_acceptable_password('ashort'))


#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False

# 07리스트 items와 정수 i를 입력받아,  만약 i가 items에 있으면 i 앞의 숫자들을 제거하고 리턴
# def remove_all_before(items, i) 
#     items=(input())
#     # 코드 작성 i값으로 items의 인덱스 번호를 알아내야함
#       if i in items
#       슬라이싱 한다.
#     return ? #items를 리턴
# def remove_all_before(items: list, i: int):
#     try:
#         return items[items.index(i):]

#     except ValueError:
#         return items

# if __name__ == '__main__':
#     print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
#     print(list(remove_all_before([1, 1, 2, 2, 3, 3], 2)))
#     print(list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)))
#     print(list(remove_all_before([1, 1, 5, 6, 7], 2)))
#     print(list(remove_all_before([], 0)))
#     print(list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)))
    
#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
#     assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
#     assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
#     assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
#     assert list(remove_all_before([], 0)) == []
#     assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]


# def easy_unpack(elements):

#     return ((elements[0],elements[2],elements[-2]))  # 튜플로 리턴
# if __name__ == '__main__':
#     print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
#     print(easy_unpack((1, 1, 1, 1)))
#     print(easy_unpack((6, 3, 7)))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
#     assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
#     assert easy_unpack((6, 3, 7)) == (6, 7, 3)


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