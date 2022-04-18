# 변수 선언
# 1. 변수이름 = 값
# 2. 변수이름1, 변수이름2, 변수이름3 = 값1, 값2, 값3
# 3. 변수이름1 = 변수이름2 = 값1

'''
num1, num2, num3 = 10, 20, 30
print(num1, num2, num3)

su1 = su2 = 100
print(su1, su2)
print(id(su1), id(su2))

su1 = 200
print(su1,su2)
print(id(su1), id(su2))

su1 = su1 + su2
print(su1, su2)
print(id(su1), id(su2))

### input()함수 : 문자열을 입력 받는 함수로 반환값은 str(문자열)***
#print(type(input()))
#print(input("입력 : "))

## 문자형 숫자 입력
num = input("숫자 입력 : ")
print('num type: ', type(num))
print('num = ', num)
print('num = ', num*2)

## 숫자 연산을 위한 형변환
num1 = int(input("정수 입력 : "))
print('num1 = ', num1*2)

num2 = float(input("실수 입력 : "))
result = num1 + num2
print('result = ', result)

## 정리, 인자(prompt)에 입력 받기 위한 설명을 사용할 수 있다.
# input()는 문자열로 입력을 받기 떄문에 숫자로 사용하기 위해서는
# 필요한 형태로 형변환을 반드시 해야한다.

## 연습... input()를 사용하여 별도의 나이와 이름을 입력 받아 다음과 같이
# 출력되게 코드를 만들어주세요. (format을 사용하세요)
# (보기)
# => '홍길동' 님의 나이는 100세 입니다.

name = input('이름 : ')
age = int(input('나이 : '))
print("'{}'님의 나이는 {}세 입니다.".format(name,age))
print(f"'{name}' 님의 나이는 {age}세 입니다.")

### 연산자
#
# (1)산술 연산자 : 산술 연산을 위해서 사용하는 연산자
#   "+(더하기)","-(빼기)","*(곱하기)","/(나누기)","//(정수나누기)","%(나머지)","**(제곱)"

nu1 = 3
nu2 = 2
print(nu1 + nu2)        # 3 + 2
print(nu1 - nu2)        # 3 - 2
print(nu1 * nu2)        # 3 * 2
print(nu1 / nu2)        # 3 / 2 -> 나누기 결과는 float(실수)t으로 반환됨.
print(nu1 // nu2)       # 3 / 2 의 몫
print(nu1 % nu2)        # 3 / 2 의 나머지
print(nu1 ** nu2)       # 3의 2제곱

# (2)비교 (관계) 연산자
# : 두 항의 값을 비교(관계)하여 관계를 설명하는 연산자 -> 반환값은 bool로 True or False 로 반환
#   값의 기준은 좌항을 기준으로 삼는다.
# "=="  : 두 항의 값이 같다.
# "!="  : 두 항의 값이 같지 않다.
# ">"   : 값이 크다.
# "<"   : 값이 작다.
# ">="  : 값이 크거나 같다.
# "<="  : 값이 작거나 같다.
# 위 관계가 맞으면 True을 반환, 틀리면 False를 반환.

print(3 == 3)       # True
print(3 != 3)       # False
print(3 > 2)        # True
print(3 < 2)        # False
print(3 >= 2)       # True
print(3 <= 2)       # False

# (3)논리 연산자 : 두 항의 값이 참인지 거짓인지 확인하여 판별하는 연산자 -> 반환값 bool
# "and(논리 곱)" : 두 항의 값이 모두 True인 경우에 True를 반환.
#   True = 1, False = 0
# "or(논리 합)"  : 두항 중 하나라도 True인 경우에 True를 반환.
# "not(부정)"    : True이면 False를 False이면 True를 반환

print("bool의 True의 int형변환 값은 : ",int(True))
print("bool의 False의 int형변환 값은 : ",int(False))

print(bool(0 and 0))     # False
print(1 and 0)     # False
print(0 and 1)     # False
print(1 and 1)     # True

print(0 or 0)     # False
print(1 or 0)     # True
print(0 or 1)     # True
print(1 or 1)     # True

print(not 0)     # True
print(not 1)     # False

# (4)멤버 연산자
#  왼쪽 피 연산자의 값이 오른쪽 연산자 멤버 중 일치 여부를 확인하는 연산자
#
# in        : 왼쪽 피 연산자의 값이 오른쪽 피 연산자에 존재하는 경우 True
# not in    : 왼쪽 피 연산자의 값이 오른쪽 피 연산자에 존재하지 않는 경우 True

print( 1 in (1,2,3))        # True
print( 1 not in (1,2,3))    # False

# (5)식별 연산자
#   식별값 비교 연산하여 처리하는 연산자.
# 
#   is      : 두 피연산자의 식별값(객체타입)을 비교하여 동일 객체라면 True 
#   is not  : 두 피연산자의 식별값(객체타입)을 비교하여 동일하지 않은 객체라면 True

num1 , num2 = 1, "1"
print(type(num1) is int)        # True
print(type(num2) is not int)    # True
print(type(num1) is not str)    # True
print(type(num2) is str)        # True

# (6)비트 연산자
# 비트값은 연산처리하는 연산자들
# &     : 두 비트 and연산처리하는 연산자(논리곱)
# |     : 두 비트 or 연산처리하는 연산자(논리합)
# ^     : 두 비트 xor연산처리하는 연산자(배타적 논리합)
# <<    : 왼쪽 피 연산자의 비트를 왼쪽으로 오른쪽 숫자만큼 이동
# >>    : 왼쪽 피 연산자의 비트를 오른쪽으로 오른쪽 숫자만큼 이동.

# & : AND 비트연산
#       00001010(10)
# &     00001101(13)
#    ===============
#       00001000(8)
print(10&13)

# | : OR 비트 연산
#       00001010(10)
# |     00000101(5)
#    ===============
#       00001111(15)
print(10|5)

# ^ : XOR 비트 연산 - 암호문 처리할 경우에 많이 사용됨
#     두 비교 비트가 동일하면 0를 반환하고, 둘중 하나라도 1이라면 1
#       00001010(10)  - 원본
# ^     00001101(13)  - 키
#    ===============
#       00000111(7)   - 암호
# ^     00001101(13)  - 키
#    ===============
#       00001010(10)  - 원본
print(10^13)
print(7^13)

# << : 왼쪽 shift연산자
#       00001010(10)
# <<              3
#       ============
#       01010000(80)
#
#  특징 : 2의 제곱승으로 곱하는 정수 곱하기

print(10<<3)

# >> : 오른쪽 shift연산자
#       00001010(10)
# >>              3
#       ============
#       00000001(1)
#
#  특징 : 2의 제곱승으로 나누는 정수 나누기
print(10>>3)
'''

'''
문제1. 
num1, num2, num3 = 5, 15, 27
    위 변수에 할당된 값을 사용하여 다음의 결과가 나오도록
    산술 연산자를 사용하시오
        ㄱ. -12
        ㄴ. 75
        ㄷ. 25
        ㄹ. 5.4
        ㅁ. 3.0
'''
'''
## 문제1
num1, num2, num3 = 5, 15, 27
# ㄱ.
print(num2 - num3)
# ㄴ.
print(num1 * num2)
# ㄷ.
print(num1 ** 2)
# ㄹ.
print(num3 / num1)
# ㅁ. 
print(num2 / num1)

'''
'''
문제2. 다음의 연산자를 보고 True와 False를 구분 하시오. 
      ㄱ. 7 > 18                False
      ㄴ. 5 < 2                 False
      ㄷ. 6 % 3 > 2             False
      ㄹ. 5 + 5 != 2 * 5        False
      ㅁ. True == 1             True
      ㅂ. 1 == '1'              False
      ㅅ. 10 // 3 == 10 % 3     False
      ㅇ. 15 % 4 in (0, 1, 2)   False
'''
'''
print(7 > 18)
print(5 < 2)
print(6 % 3 > 2)
print(5 + 5 != 2 * 5)
print(True == 1)
print(1 == '1')
print(10 // 3 == 10 % 3)
print(15 % 4 in (0, 1, 2))
'''
'''
문제3. input()으로 2개의 값을 받은 다음 더하기, 빼기, 곱하기, 나누기 연산을 
    하여 그 결과를 출력하는 코드를 작성하시오.
'''
'''
number1 = int(input("숫자 : "))
number2 = int(input("숫자 : "))
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
'''
'''
문제4. 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 출력하는 
    코드를 작성하시오.
    
    비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
    표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9

    출력 예제 : 홍길동님의 비만도는 112.15% 입니다.
'''
'''
name = input("이름 : ")
height = float(input("키 : "))
kg = float(input("체중 : "))

std = (height - 100) * 0.9
fat = kg / std * 100

print("{}님의 비만도는 {:.2f}% 입니다.".format(name, fat))
'''
#### 제어문(if), 반복문(for,while)
# 제어문(if)
#
# 단순 if
#   사용형식1
# if 조건식 : 
#     실행문(종속문장1)
#     실행문(종속문장2)     => if 블럭

# 특징 : 조건식이 참일 경우에 종속 문장을 실행
#       파이썬에서는 다른 언어와 다르게 들여쓰기가 중요함.
#       들여쓰기를 가지고 블럭을 구분함......

# [예제1]
num = int(input("정수 입력 : "))
if num % 2 == 0:
    print("num 변수에 값은 짝수 입니다.")
    print("num 변수의 값은 2의 배수입니다.")
print("if 다음 문장 실행")

# [예제2]
print("1. Easy Game")
print("2. Hard Game")
print("3. Exit")
num = int(input("번호선택>> "))
if num == 1:
    print("Easy Game Start")    
if num == 2:
    print("Hard Game Start")
if num == 3:
    print("Game Exit")    
    
# [예제3]
su = int(input("수 입력 : "))
if su == 1:
    print("1 입력")
if su > 10 :
    print("10보다 큰 수를 입력했습니다.")
if su < 10 :
    print("10보다 작은 수를 입력했습니다.")
    
# [예제4]
x = 15
if x > 10 and x != 10:
    print("x변수의 값은 10보다 크고 , 10과 같지 않다.")
else:
    print("x는 10보다 크고, 15와 같다.")
    
# [예제5]
su = int(input("1 ~ 10 사이의 정수를 입력하세요 : "))
if su in (1, 4, 7):
    print("멤버에 있는 숫자입니다.")
    
# if ~ else : if의 조건식이 참이면, if의 종속문장을 그렇지 않으면 else의 종속문장을 실행
#   사용형식1
# if 조건식 : 
#     실행문(종속문장1)
#     실행문(종속문장2)     => if 블럭
# else:
#     실행문(종속문장1)
#     실행문(종속문장2)     => else 블럭 둘다 합쳐 하나의 if문으로 처리


'''
[ IF문 문제 ]
1. 입력한 데이터가 3의 배수인 경우 출력하시오
2. 절대값을 구하는 프로그램을 작성하시오.
3. 수를 입력 받아 짝,홀수를 구분하여 출력하시오.
4. 두수를 입력 받아 큰 수를 출력하시오.
5. 세수를 입력 받아 큰 수를 출력하시오.
6. 두수를 입력 받아 큰 수가 짝수이면 출력하시오.
7. 두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오.
'''
# 1. 입력한 데이터가 3의 배수인 경우 출력하시오
num = int(input("숫자를 입력하세요 : "))
if num % 3 == 0:
    print(f"{num}은 3의 배수입니다.")
else:
    print(f"{num}은 3의 배수가 아닙니다.")

# 2. 절대값을 구하는 프로그램을 작성하시오.
num = int(input("숫자를 입력하세요 : "))
if num < 0:
    print(-num)
if num > 0:
    print(num)
    
# 3. 수를 입력 받아 짝,홀수를 구분하여 출력하시오
num = int(input("숫자를 입력하세요 : "))
if num % 2 == 0:
    print(f"{num}은 짝수입니다.")
else:
    print(f"{num}은 홀수입니다.")

# 4. 두수를 입력 받아 큰 수를 출력하시오.
num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))

if num1 > num2:
    print(f"{num1} 이(가) {num2} 보다 더 큽니다.")
else:
    print(f"{num2} 이(가) {num1} 보다 더 큽니다.")
if num1 == num2:
    print("두 수는 같습니다.")
    
# 5. 세수를 입력 받아 큰 수를 출력하시오.
num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))
num3 = int(input("세번째 숫자를 입력하세요 : "))
if num1 > num2 and num1 > num3:
    print(f"{num1} 이(가) 제일 큽니다.")
if num2 > num1 and num2 > num3:
    print(f"{num2} 이(가) 제일 큽니다.")
if num3 > num1 and num3 > num2:
    print(f"{num3} 이(가) 제일 큽니다.")
    
# 6. 두수를 입력 받아 큰 수가 짝수이면 출력하시오.
num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))
if num1 > num2 and num1 % 2 == 0:
    print(f"{num1}은 {num2}보다 크고 짝수입니다.")
if num2 > num1 and num2 % 2 == 0:
    print(f"{num2}은 {num1}보다 크고 짝수입니다.")
        
# 7. 두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오.
num1 = int(input("숫자를 입력하세요 : "))
num2 = int(input("숫자를 입력하세요 : "))
if (num1 + num2) % 2 == 0 and (num1 + num2) % 3 == 0:
    print(f"{num1}과 {num2}의 합은 짝수이고 3의 배수입니다.")
else:
    print(f"{num1}과 {num2}의 합은 짝수가아니고 3의 배수도아닙니다.")
    
# 중첩 if 구문 : if 구문 안에 if 구문을 사용하는 경우
# 다중 if 구문 : if ~ elif ~ else 구문으로 if와 elif 조건을 확인 부합되면 종속 실행.
#               만약 조건에 부합되지 않는 경우에는 else를 실행.

# [예제7] 중첩 if 구문
num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))
Sum = num1 + num2
if Sum % 2 == 0:
    if Sum % 3 == 0:
        print(f"입력하신 두 수의 합은 {Sum}, 3의 배수이면서 짝수입니다.")
    else:
        print(f"입력하신 두 수의 합은 짝수이지만, 3의 배수는 아닙니다.")
else:
    print("입력하신 두 수는 짝수가 아닙니다.")


# [예제8] 다중 if 문 (if ~ elif ~ else)
num = int(input("1 ~ 4 숫자를 입력 : "))
if num == 1:
    print("1 입력")
elif num == 2:
    print("2 입력")
elif num == 3:
    print("3 입력")
elif num == 4:
    print("4 입력")
else:
    print("잘못 입력했습니다.")
    
'''
[Quiz1]
- 사용자로 부터 Gbyte의 값을 입력받아 byte,kbyte,Mbyte로 각각 출력 되게 만드시오
- (1.byte 2.kbyte 3.Mbyte 선택)
- 단위 1024
'''
Gbyte = int(input("Gbyte값 입력 : "))
num = input("1.byte 2.kbyte 3.Mbyte 선택 : ")
byte = Gbyte * (1024**3)
kbyte = Gbyte * (1024**2)
Mbyte = Gbyte * 1024

if num == '1':
    print("{:,}Gbyte는 {:,}byte입니다.".format(Gbyte,byte))
elif num == '2':
    print("{:,}Gbyte는 {:,}kbyte입니다.".format(Gbyte,kbyte))
elif num == '3':
    print("{:,}Gbyte는 {:,}Mbyte입니다.".format(Gbyte,Mbyte))
else:
    print("잘못 입력했습니다.")

'''
[Quiz2]
- 인증 프로그램을 만드시오
1. 아이디가 틀리면 등록되지 않은 아이디 입니다 출력
2. 비밀번호가 틀리면 비밀번호가 틀렸습니다 출력
3. 아이디와 비밀번호가 일치한다면 인증 통과 출력
-old_id = test, old_pw = python123
'''
old_id = 'test'
old_pw = 'python123'

print("인증 프로그램 시작")
new_id = input("아이디 입력 : ")
new_pw = input("비밀번호 입력 : ")

if old_id == new_id:
    if old_pw == new_pw:
        print("인증 통과")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("등록되지 않은 아이디 입니다.")

## 삼항 조건문 : 삼항 연산자, 조건식이 참인 경우와 거짓인 경우 처리할 문장을 한줄로 작성
# 조건식 비교 결과에 따라 선택적으로 실행문이 동작합니다.
#
#   (형식)
#   변수 = 참 if (조건문) else 거짓

# 삼항 조건문 예제
# 1)일반 조건문
num = 9
result = 0

if num >= 5:
    result = num * 2
else:
    result = num + 2

print("result = ", result)

print("3항 연산자")
result2 = num * 2 if num >= 5 else num + 2
print("result2 = ",result2)

'''
문제4. 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 출력하는 
    코드를 작성하시오.
    
    비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
    표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9
    
    비만도가 100 미만인 경우  : "저체중"
    비만도가 100 ~ 110 사이인 경우 : "정상 체중"
    비만도가 110 ~ 120 사이인 경우 : "과체중"
    비만도가 120 ~ 130 사이인 경우 : "비만"
    그 이상인 경우 "고도비만"으로 표현되게 작성하세요.

    출력 예제 : 홍길동님의 비만도는 112.15%로 정상체중 입니다.
'''
name = input("이름 : ")
height = float(input("키 : "))
kg = float(input("체중 : "))

std = (height - 100) * 0.9
fat = kg / std * 100

if fat <= 100:
    print("{}님의 비만도는 {:.2f}% 저체중 입니다.".format(name, fat)
elif fat > 100 and fat <= 110:
    print("{}님의 비만도는 {:.2f}% 정상 체중 입니다.".format(name, fat)
elif fat > 110 and fat <= 120:
    print("{}님의 비만도는 {:.2f}% 과체중 입니다.".format(name, fat)
elif fat > 120 and fat <= 130:
    print("{}님의 비만도는 {:.2f}% 비만 입니다.".format(name, fat)
else:
    print("{}님의 비만도는 {:.2f}% 고도비만 입니다.".format(name, fat)

# 월요일 실습 문제 제공 if, 반복문 학습







