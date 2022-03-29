'''
# 문제 6] 다음과 같은 모형으로 출력되게 하세요. (단, 파이썬 서식은 사용안함.)
6-1         6-2         6-3         6-4
*           *****           *       *****
**          ****           **        ****
***         ***           ***         ***
****        **           ****          **
*****       *           *****           *
'''
# 6-1
for i in range(5):  # [0,1,2,3,4]
    for j in range(i+1):    #[1,2,3,4,5]
        print("*",end='')
    print()     # 줄 바꿈
print()

# or
i = 0
while i < 5:
    x = 0    # 하위 반복문 초기값
    j = i + 1   
    while x < j:
        print("*",end='')
        x += 1
    print()
    i += 1
print()

# 6-2
for i in range(5): # [5,4,3,2,1]
    for j in range(5 - i):  # [5,4,3,2,1]
        print("*",end='')
    print()
print()
    
# 6-3
for i in range(5):
    for j in range(4-i):   # 공백을 처리하는 반복문
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()    
    
# 6-4
for i in range(5):
    for j in range(i):
        print(" ",end='')
    for j in range(5-i):
        print("*",end="")
    print()
    

'''
6-5 출력 줄수를 입력하면 다음과 같이 출력
  입력 줄은 홀수이여야만 함.
   hint : 별, 공백, 줄수, 반복문을 위한 변수, flag
   
홀수 줄수를 입력 : 7
   *           st : 줄이 바꿀때 마다 +2(줄수의 반)/반 넘으면, -2
  ***          sp : 줄수를 //2 (초기값), 줄수의 반전 -1, 후 +1
 *****
*******
 *****
  ***
   *
'''
import os   # os 모듈은 파이썬에서 기본 제공하는 기본 라이브러리 모듈로
            # os 와 관련된 함수들이 저장된 모듈
            # system() => os의 시스템 명령어를 사용할 수 있게 함.
import time # 시간과 관련된 제공하는 기본 라이브러리 모듈

i, j = 0, 0; num = 1
while num :
    os.system('cls')
    ln = int (input("홀수 줄수를 입력 : "))
    sp = ln // 2; st= 1; flag = True
    for i in range(ln):
        for j in range(sp):
            print(end=' ')  # 빈 공간 찍기
        for j in range(st):
            print(end='*')   # 별 찍기
        print() # 줄 바꿈
        if i == (ln//2):
            flag = False
        if flag:
            sp -= 1
            st += 2
        else:
            sp +=1
            st -= 2
    num = int(input("계속 하겠습니까?(0.종료, 1.계속) : "))    
    
## 랜덤 함수
#   : 임의의 값(난수)을 출력하는 함수
#   난수는 생성된 임의의 값을 의미한다.
# 
#   랜덤 함수를 사용하기 위해서 모듈을 사용 : random
#   
#   모듈 사용 방법 : import [모듈명]
#   ex) import random      # 랜덤 모듈 전체를 로딩
#   or
#   ex) from [모듈] import [모듈에 있는 내용]   # 모듈 내에 일부 정보를 로드
#       from random[모듈] import random[함수].  # 랜덤 모듈 내에 random() 함수를 로드
#   두 방식은 기능 사용방식에 차이가 존재함
#   import 모듈인 경우 , [모듈명].[사용할 값]
#   from [모듈] import [모듈에 사용할 값]인 경우, 모듈에 사용한 값을 그대로 사용

from random import random
print(random())    # random모듈에 있는 random()함수
                   # 0.0 ~ 1.0 미만의 임의 값을 출력(float)
print(random()*10) # 0.0 ~ 10.0 미만의 임의 값을 출력(float)
print(int(random()*10))     # 0 ~ 10미만의 값을 출력(int)
print(int(random()*10)+1)   # 1 ~ 10까지의 값을 출력(int)

# 예제 1] 1 ~ 45 까지의 임의 값 6개를 출력
from random import random

for i in range(6):
    print(int(random()*45)+1, end=' ')  # 임의의 1 ~ 45 사이의 숫자
    
# 문제 1] 1 ~ 100 까지 랜덤 값을 6개 출력하는 코드 작성
from random import random

for i in range(6):
    print(int(random()*100)+1, end=" ")
    
# 문제 2] 1 ~ 100 까지의 랜덤 값을 반복하여 출력하되, 출력 값이 50이 출력되는 순간
#         반복이 종료되는 코드를 작성하세요.
from random import random
while True:
    num = int(random()*100)+1
    print(num,end=' ')
    if num == 50:
        break
print()

# 문제 3] 1 ~ 15 까지 랜덤 값을 중복 없이 3개 생성하여 출력하는 코드 작성
from random import random

num1, num2, num3 = 0,0,0

while True:
    su = int(random()*15)+1
    if num1 != su:
        num1 = su
        break

while True:
    su = int(random()*15)+1
    if num1 != su and num2 != su:
        num2 = su
        break

while True:
    su = int(random()*15)+1
    if num1 != su and num2 != su and num3 != su:
        num3 = su
        break
    
print(num1,num2,num3,end=' ')
    
# random 모듈 내에 있는 다른 형태의 random 함수들...
# -randint() : 임의의 값을 출력하는 int값 랜덤 함수
# 
#  사용방법
#     randint(a,b)
#       a : 시작값, b : 마지막값  => 시작값부터 마지막값까지의 랜덤
#  예제 2] 1 ~ 6 까지의 임의의 값 출력하는 예제
from random import randint

print(randint(1,6))
print(randint(100,200))

# 또 다른 random함수
#   - randrange() : 범위 내에 있는 임의 값을 출력
#
#    예시1)
#     randrange(5,10)   => 5 ~ 10 미만의 값을 출력 ([5,6,7,8,9] 중 하나)
#    예시2)
#     randrange(5,10,2) => 5 ~ 10 미만까지 2씩 증가 값을 출력 ([5,7,9] 중 하나)

# 예제 3]
from random import randrange
print(randrange(10))
print(randrange(5,10))
print(randrange(5,10,2))

# random 모듈 내에 choice() 함수
# : 이 함수의 특징은 리스트와 같은 형태의 자료 중 일부를 랜덤하게 추출하는 함수
#
# 예시)
# dice = [1,2,3,4,5,6]  # 리스트형
# choice(dice)  # dice 리스트 내에 있는 맴버중 하나를 추출하여 출력
#

# 예제 4]
import random
dice = [1,2,3,4,5,6]
st = 'Hello world'
x = random.choice(st)
print("dice에서 출력된 값 : ",x)

# or

from random import choice,random,randint,randrange
dice = [1,2,3,4,5,6]
st = 'Hello world'
x = choice(st)
print("dice에서 출력된 값 : ",x)


# 문제 4] 1 ~ 99 까지 랜덤 값 중에 짝수는 True,
# 홀수면 False 출력하는 프로그램 코딩
from random import random
print("출력 결과 : ",end="")
rand = int(random()*99)+1
if rand % 2 == 0:
    print(f"True({rand})")
else:
    print(f"False({rand})")

'''
ASCII 코드
 미국 표준 문자 코드로 7bit(0 ~ 127)로 하나의 문자를 표현할 수 있음.
ASCII코드는 통신상 기본 문자 코드로 사용되고 있음.

(특징)
1. 프린트 가능한 문자 총 95자, 나머지 33개 문자는 프린트가 불가능한 문자.
   프린트 가능한 문자의 시작 0x20(32) -> "공백"부터 시작, 0x7e(126)까지 임.
2. 숫자는 0x30(48)="0"에서부터 0x39(57)="9"까지 값을 가진 10개의 코드
3. 영문 대문자는 0x41(65) => "A"에서부터 0x5A(90) ="Z" 까지
4. 영문 소문자는 0x61(97) => "a"에서 0x7A(122)="z"까지
5. ASCII코드는 문자이나 숫자(정수)로 표현이 가능함.

숫자를 문자(ASCII)코드로 변경하는 함수 : chr()
    ()안에 코드 값을 전달하면 그 값을 문자로 출력하는 함수
'''

print(chr(65))  # A
print(chr(0x41))    # A

# 문제 5] 'A' ~ 'Z' 까지의 임의 문자 3자리를 출력하는 코드를 작성하세요 !!!
from random import randint
for i in range(3):
    st = int(randint(65,90))
    print(chr(st),end=' ')
    
# or
from random import randint, random, randrange, choice

for x in range(3):
    ch = int(random()*26)+65
    print(chr(ch),end=' ')
    
# LIST
# 리스트 자료형이란?
#   -데이터 목록을 다루는 자료형
#   -리스트를 정의할 때는 "[]"를 사용함.
#   -리스트 안에는 어떤 종류의 자료형이든 상관없이 저장 가능.
#
# List 자료형의 기본 사용(정의)
#
# (정의)
#  변수명 = []      # 비어있는 리스트를 선언
#  변수명 = [value1, value2, value3, value4, ...]
#  (value들의 타입은 상관없이 가능)
#
# (list()를 이용한 리스트 생성)
#  변수명 = list()  # 비어있는 리스트를 선언
#  변수명 = list("Hello")   # ['H','e','l','l','o'] 
#  변수명 = list(range(5))  # [0,1,2,3,4]

# 예제 1] 리스트 선언 및 값에 대한 처리
lst = [1,2,3,4,5,6,7,8]
print(type(lst))
# 생성된 리스트에 대한 특정 값 참조 : 인덱스(index)값을 이용
# indexing방법 : 변수명[인덱스값]   # 주의) 인덱스 값의 시작은 0부터 시작
print(lst[0])       # 1
print(lst[3])       # 4

# 인덱싱을 이용한 list값 변경
lst[0] = lst[5]     
print(lst[0])
print(lst)

# 리스트 자료의 길이 (요소[멤버]의 갯수) : len()
print("lst의 길이 : ",len(lst))

# 리스트의 결합1(병합)
lst2 = [9,10]
print(lst + lst2)   # [ 6, 2, 3, 4, 5, 6, 9, 10]
lst3 = lst + lst2
print(lst3)

# 리스트의 결합2(확장)
lst = lst + lst2
print(lst)          # [ 6, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트의 반복
print(lst2 * 3)     # [ 9, 10, 9, 10, 9, 10]

# max() : 최댓값, min() : 최솟값
# lst = [ 6, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(lst))     # 10
print(min(lst))     # 2
print(sum(lst))     # 60
print(pow(2,2))     # 4  앞 숫자를 뒷 숫자의 제곱형으로 사용 2의 2제곱

# 변수를 선언, 3개의 정수를 입력 받아 합을 출력 코딩
# 출력 결과 >> "합계" = xx" <"합계"문자도 변수로 저장하여 사용>

a = int(input("첫번째 정수 : "))
b = int(input("두번째 정수 : "))
c = int(input("세번째 정수 : "))
d = "합계"
Sum = a + b + c

print(f"{d} = {Sum}")

# 예제 2] 리스트의 맴버를 변수처럼 사용
lst = [0, 0, 0,'합계']
lst[0] = int(input("첫번째 정수 : "))
lst[1] = int(input("두번째 정수 : "))
lst[2] = int(input("세번째 정수 : "))
Sum2 = lst[0] + lst[1] + lst[2]
print(f"{lst[3]} = {Sum2}")

# List 인덱싱
#   : 인덱스 값을 이용한 참조
#
#       lst = [ 1, 2, 3, 4, 5, 6, 7, 8]
# 양의 index :  0   1   2   3   4   5   6   7 
# 음의 index : -8, -7, -6, -5, -4, -3, -2, -1

# (-1) => 11111111 11111111 11111111 11111111
# (-2) => 11111111 11111111 11111111 11111110

# 예제 3] List 인덱싱
lst = [ 1, 2, 3, 4, 5, 6, 7, 8]
# (+) :  0   1   2   3   4   5   6   7 
# (-) : -8, -7, -6, -5, -4, -3, -2, -1
print("lst[] : ",lst)
print("lst[-1] : ",lst[-1])
print("lst[-2] : ",lst[-2])
print("lst[-3] : ",lst[-3])

# slicing방식을 이용한 시퀀스 객체(자료) 접근
# slicing이란? 리스트와 같은 시퀀스 자료 값들의 범위로 접근하기 위해서
#       사용하는 방법으로 시퀀스 자료의 일부를 잘라서 새롭게 생성하는 것을 의미함.
# 
#  (형식)
#   변수명[시작인덱스:끝인덱스]
#   변수명[시작인덱스:끝인덱스:증감값]
#
#  예] 
#  lst = [ 1, 2, 3, 4, 5, 6]
#  index   0  1  2  3  4  5
#   (-)   -6 -5 -4 -3 -2 -1
#
#  lst[0:3]  => [1,2,3], lst[0,3,2] = [1,3]
lst = [ 1, 2, 3, 4, 5, 6]
print(lst[0:3])
print(lst[0:3:2])
print(lst[-6:-3])
print(lst[-1:-3:-1])
print(lst[5:0:-3])

# 인덱스 생략
print(lst[:3])      # 시작값 생략 : [1, 2, 3]
print(lst[3:])      # 끝값 생략 : [4, 5, 6]
print(lst[:])       # 둘다 생략 : [1, 2, 3, 4, 5, 6]

# 슬라이싱 후 새로운 리스트 생성
slc1 = lst[3:6]     # [4,5,6]
print(slc1)
slc2 = lst[1:5:3]   # [2,5]
print(slc2)
slc3 = lst[5::-1]   # [6,5,4,3,2,1]
print(slc3)
slc4 = lst[-3:-1]   # [4,5]
print(slc4) 

# 리스트 함수들 ...
#   - append(value) : 리스트 끝에 값을 추가(멤버 추가)
#   - extend(iter)  : 리스트 끝에 list,tuple,dict의 값을 하나씩 추가
#   - insert(idx,value) : idx(인덱스)에 있는 인덱스 위치에 특정값을 추가하는 함수
# =============== 위 3개는 리스트에 값을 추가하는 메서드
#   - pop([idx]) : 인덱스를 지정하지 않으면, 마지막 인덱스 값을 반환후 삭제
#                   인덱스 값을 지정하면, 해당 인덱스 값을 반환 후 삭제
#   - remove(value) : 특정 값을 찾아서 삭제하는 함수
#   - clear() : 리스트의 모든 맴버를 삭제하고, 빈 리스트로 만드는 함수
# =============== 위 3개는 리스트에 값을 제거하는 메서드
#   - count(value) : 리스트 내에 특정 값의 개수를 반환하는 함수
#   - index(value) : 리스트 내에 특정 값의 인덱스 값을 반환하는 함수
#   - reverse() : 리스트의 맴버의 순서를 뒤집어서 나열하는 함수
#   - sort([reverse=False]) : 리스트의 값을 오름차순(False)
#                             내림차순(True) 정렬해주는 함수
# print(help('list'))

# append() : 리스트 끝에 값을 추가
lst1 = [1,2,3,4,5,6,7,8]
lst1.append('a')
print(lst1)             # [1, 2, 3, 4, 5, 6, 7, 8, 'a'] => len(lst1) -> 9
lst1.append([9,10])     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', [9, 10]] -> len(lst1) -> 10
print(lst1)
print(lst1[-1])

# extend() : 리스트 뒤에 추가할 리스트, 튜플, 딕셔너리 자료를 맴버에 개별적 추가
lst1 = [1,2,3,4,5,6,7,8]
lst1.extend('abcdef')
print(lst1)

# insert(idx,value) : idx인덱스 위치에 값을 추가
lst1 = [1,2,3,4,5,6,7,8]
# idx : 0 1 2 3 4 5 6 7 
lst1.insert(3,'a')
print(lst1)            # [1,2,3,'a',4,5,6,7,8]

# pop() : 맨 뒤에 있는 맴버 반환후 삭제,
#         idx 값을 넣으면 해당 인덱스 값을 반환 후 삭제
lst1 = [1,2,3,4,5]
a = lst1.pop()
print(a)               # a = 5, lst1 => [1,2,3,4]
print(lst1)
b = lst1.pop(2)
print(b)               # b = 3, lst1 => [1,2,4]
print(lst1)

# remove(vlaue) : value에 있는 내용을 검색 후 삭제
#                 검색시에 없으면 Error를 반환
lst1 = [1,2,3,2,5,6,2,8]
lst1.remove(2)          # 첫번째 2가 삭제됨
print(lst1)             # [1,3,2,5,6,2,8]
lst1.remove(2)          # 두번째 2가 삭제됨
print(lst1)             # [1,3,5,6,2,8]
lst1.remove(2)          # 세번째 2가 삭제됨
print(lst1)             # [1,3,5,6,8]
# lst1.remove(2)          # ValueError : list.remove(x) : x not in list

# clear()
lst1 = [1,2,3,4,5]
lst1.clear()
print(lst1)

## 여기 이후, count, index, reverse, sort