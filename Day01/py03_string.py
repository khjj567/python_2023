# 문자열

value = "hello world"
print('hello world')
print(value)


# 따옴표안에 따옴표
print('저는 "어쩌구" 입니다')
print("저는 '어쩌구' 입니다")

# 여러줄 문장
# 홑따옴표 3개 써도 쌍따옴표 3개 써도 똑같다
value = '''
안녕하세요 저는
어쩌구저쩌구 
프로그래머입니다
'''
print(value)

'''
여러줄 주석으로 쓰인다
파이썬에는 여러줄 주석이 없어서 여러줄 문자열이 이 역할을 대신한다
이걸 변수에 할당하지 않으면 무시할 수 있는게 되서 가능하다
'''

# 문자열 연산 
# 문자열 더하기 문자열 가능
# 곱하기는 해당 문자열을 뒤에수만큼 프린팅 가능
# 더하기는 안돼
# 문자열 곱하기 문자열 안돼
print('Hello' + " world!") # Hello world!
# print('Hello' + 4) #TypeError: can only concatenate str (not "int") to str
print('Hello!' * 4) # Hello!Hello!Hello!Hello! 반복

# 문자열의 길이
# 공백과 점을 다 샌다
print(len('Life is short'))
print(len('인생은 짧아요.')) 

# 문자열 슬라이싱
origin = 'Life is short, you need python'
print(origin[14]) # 공백도 나오고 점도 나온다
print(origin[0] + origin[1] + origin[19] + origin[20]) # 인덱스로 단어를 조합할수도 있다
print(origin[0].lower()) # 소문자
# 0부터 n까지 자르기
print(origin[0:4]) # == print(origin[:4])
# n부터 n까지 자르기
print(origin[8:13])
print(origin[15:]) # index 15부터 끝까지
print(origin[15:-8]) # 뒤에서부터 샐때는 음수로 샌다 #다른 언어는 음수는 0 앞을 말한다.

# 문자열 포매팅
print("I ate %s apples" % ('three')) # s : String 
# => I ate three apples
print("I ate %d apples" % (3)) # d : t숫자
print("pi is %f" % 3.1415926593) # 부동소수(floating-point)
print("pi is %10.2f" % 3.1415926593) # % String formating

# 날짜 문자열 포매팅
import datetime as dt
curr_dt = dt.datetime.now()
print(curr_dt)
print('오늘 날짜는 %s' % curr_dt.strftime('%Y년 %m월 %d일')) # strftime : curr_dt는datetype => string으로 바꾸는 포맷
# C# yyyy월MM년dd일
# JAVA yyyy월MM년dd일

# 최신 포매팅
apple_num = 3
print(f'I ate {apple_num} apples')
print(f'I ate {apple_num:0.4f} apples') # => I ate 3.0000 apples
apple_num = 'three'
print(f'I ate {apple_num} apples')
fmt_dt = curr_dt.strftime('%Y년 %m월 %d일')
print(f'오늘 날짜는 {fmt_dt} 입니다')

# 문자열 함수
print(origin.count('o')) # => 3  : 문자 혹은 문자열의 개수 : 단어나 문장 문자 모두 찾을 수 있다
print(origin.count('w')) # 
print(origin.find('python')) # 문자 문자열 찾는 시작인덱스 -1없음
print('/'.join(origin)) # 문자(열) join에 있는 문자열이랑 하나씩 합치는 함수
print(origin.upper()) #전부 대문자
print(origin.lower()) #전부 소문자
print(origin.capitalize()) # 시작단어 첫번째 문자만 대문자로
print(origin.title()) # 단어의 첫번째 글자를 대문자로

print('test','    Hello    ','end')
print('test'+'    Hello    '.lstrip()+'end') # 왼쪽 공백 지우기 lstrip
print('test'+'    Hello    '.rstrip()+'end') # 오른쪽 공백 지우기 lstrip
print('test'+'    Hello    '.strip()+'end') # 모든 공백 지우기 lstrip

result = origin.replace(',', '').split(' ') # 쉼표 빼고 공백으로 자르기 => 배열(리스트)
print(result)

