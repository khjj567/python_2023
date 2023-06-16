# 변수

number = 10
print(number)

# 맨 아래만 나오는게 아니라 print 다 나옴
number = 111
print(number)

# 파이썬은 숫자 사이즈에 제약이 없다
number = 210000000000000000000000000000000
print(number)

import sys # -> 라이브러리 부르기 시스템에서 쓰고싶은거 부르기
value = sys.maxsize # 파이썬 시스템이 제공하는 최고숫자
print(value) # 9223372036854775807
print(value+1) # 9223372036854775808 (?) => 시스템이 가진 최고사이즈가 있지만 한계 없다

value2 = 0o12 #8진수
print(value2)

value2 = 0xFF #16진수
print(value2)

value2 = "0xFF #16진수"
print(value2)

value2 = False
print(value2 == False)

# 사칙연산 및 수학식
print(3-5) # -도 나옴
print(14/2) # 소숫점 나옴 (근데 도중에 반올림으로 32.444444444445 : 값의 불명확함)
print(13//2) # 소숫점 안나옴 (몫만 나오더라)
print(13%2) # (나머지만 나옴)
print(2**10) # 2의 10승 = 1024

