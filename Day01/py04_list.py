# 리스트

import datetime
value = datetime.datetime.now()
lists = [1,2,3,4,[5,6,7,8],True,'hello', value] # 리스트에 뭐든지 넣을 수 있다
print(lists)
print(lists[-2]) #배열 뒤에서 두번째

print(lists[4][1]) # 배열안에 배열 => 6
print(lists[-2][-1]) # 배열 안에 문자열 => o
# print(lists[-1][-1]) # 오류난다

# 리스트슬라이싱
print(lists[:4]) # 두번째 값은 찾고 싶은 값(들)의 마지막 인덱스+1(파이썬만)
#리스트의 연산
a=[1,2,3]
b=[4,6,8] # => [1, 2, 3, 4, 6, 8]
print(a+b) # => [1, 2, 3, 1, 2, 3]
print(a*2)
a[2] = False # 2번 인덱스값을 False로 바꾸면
print(a) # => [1, 2, False]
del b[2] # 2번 인덱스를 지우면
print(b)

# 리스트함수 (문자열함수만큼 중요)
c=[3,6,9]
c.append(12)  # 마지막에 값 추가함수 
print(c)

d = [6,4,9,3,2,4]
d.sort() # 정렬함수 : 문자열도 정렬이 가능함 : 
print(d) # => [2, 3, 4, 4, 6, 9]

e = [2,5,43,1,8,4]
e.reverse() # 역정렬x. 순서를 뒤집는것. 
print(e) # =>[4, 8, 1, 43, 5, 2]

e.sort(reverse=True) # 역정렬(내림차순정렬)
print(e) # =>[43, 8, 5, 4, 2, 1]

# 인덱스 반환
print(e[1]) # 인덱스로 리스트에서 값을 찾기
print(e.index(43)) # 리스트의 값으로 인덱스를 찾기

e.insert(2,5.5) # 2번인덱스에 5.5를 추가하기
print(e)

e.append(8) # 이미 있는 8을 추가한다(뒤에)
print(e)
e.remove(8) # 앞에 8부터 지워진다
print(e)