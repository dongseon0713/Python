## 변수 자료형...
# "#"은 한줄 주석...
# "''' ~ '''"와 같은 처음 '세개와 뒤 '세개 사이는 다중 문자열 처리되면서 주석과 같은 처리

# 여러줄 주석 처리 -> 자바 : //
'''
 여기에 입력된 값들은
 모두 다중 문자열로 처리되어 실행 코드와 상관 없는 데이터가 됨
    /* ~ */
'''

"""_summary_
 여기에 사용하는 것도 서머리로 사용되면서 실행 코드가 아닌 값이 됩니다.


# 변수 : 필요한 데이터를 일시적으로 보관하거나 처리 결과를 담을 수 있는 기억 장소
# 파이썬에서는 이 변수가 값을 저장하는 것이 아니라, 저장된 값의 주소 메모리 주소를 저장한다는
# 특징을 갖고 있다.

# 변수의 작명 규칙
# - 의미를 파악할 수 있는 이름으로 지정
# - 첫자는 영문자 또는 "_"로 시작한다. (숫자가 처음에 시작되지 않는다.)
# - 공백이나 특수문자는 사용하지 않는다.
# - 예약어를 사용할 수 없다.(예약어는 이미 사용되고 있는 명령어들)
# - 대문자와 소문자는 서로 다른 변수 인식(대소문자 구분)
# - 두 단어를 조합하여 변수명을 지정할 경우 두번째 단어의 첫글자는 대문자로 표기.

var1 = "Hello Python"
print(var1)
# id() -> 내장함수로 메모리 주소를 알려준다.
print(id(var1))     # var1이 가리키는 데이터의 메모리 주소를 알려줌

var2 = 100
print(var2)
print(id(var2))

var3 = 100.234
print(var3)
print(id(var3))

var4 = True
print(var4)
print(id(var4))

import keyword # 모듈 임포트
python_keyword = keyword.kwlist
print(python_keyword)

# 데이터 타입을 알려주는 내장 함수 : type()
# 데이터의 길이 값을 알려주는 내장함수 : len()
print(type(python_keyword)) # 데이터타입
print(len(python_keyword))  # 데이터의 갯수

## 파이썬의 자료형
# 문자형 자료 - str : ''또는 ""를 이용하여 표기
# 숫자형 자료 - 정수(int), 실수(float) : 10(int), 10.123(float)
# 논리형 자료 - Bool(ean) : True, False

#--자료구조 : list, dict, tuple, set

var1 = "Hello Python"
print(var1)
print(type(var1))   # str -> <class 'str'>

var2 = 100
print(var2)
print(type(var2))   # int -> <class 'int'>

var3 = 100.234
print(var3)
print(type(var3))   # float -> <class 'float'>

var4 = True
print(var4)
print(type(var4))   # Bool(ean) -> <class 'bool'>

# 자료형 변환
# : 형변환은 묵시적 형변환, 명시적 형변환 두가지 형태를 가지고 있음. 
# 묵시적 형변환은 작업하지 않아도 프로그램에서 자동으로 변환하는 형변환
# 명시적 형변환은 형변환에 대한 내용을 명시적으로 처리하는 형변환

test1 = 1 + 1.0
test2 = 1 * 1.0
print(type(test1))
print(type(test2))
# test3 = 1 + '1'     # 에러 발생 : 문자를 숫자로 변환이 안됨.

# 명시적 형변환 함수들 : int(), float(), str(), bool(), .... list(), tuple(), dict() .... 
print("int형 변환")
a = int(10.5)
print(type(a), a)

b = int('100')
print(type(b), b)

# c = int('100.1')    # ValueError 발생, why? int()는 한번만 변경하기 때문에....
# print(type(c), c)

# int(x, base=int(숫자)) base인자 값은 정수 표현 방식을 결정....
print(int('1010',base=2))   # 10
print(int('10',base=8))     # 8
print(int('10',base=16))    # 16
print(int('1C',base=16))    # 28

# 2. float() : 문자, 정수 -> 실수
print(float('1001'))        # 1001.0
print(float(1001))          # 1001.0
print(float('1001.100'))    # 1001.1

# 3. bool() : 논리형 형변환
# bool은 특정 값을 제외하고, 모두 True

# -정수-
print(bool(1))              # True
print(bool(0))              # False
print(bool(-1))             # True

# -실수-
print(bool(1.0))            # True
print(bool(0.0))            # False
print(bool(0.1))            # True

# -문자열-
print(bool('a'))            # True
print(bool(''))             # False

# -비교연산식-
print(bool(1>0))            # True
print(bool(1<0))            # False

# -list
print(bool([1,2,3,4,5]))    # True
print(bool([]))             # False

# -tuple
print(bool((1,2,3,4,5)))    # True
print(bool(()))             # False

print(int(True))            # 1
print(int(False))           # 0

# 진수 표현... 정수 추가변환
# bin(), oct(), hex() 함수의 사용
print(bin(10))              # 0b1010   -> 2진수 값
print(oct(10))              # 0o12     -> 8진수 값
print(hex(10))              # 0xa      -> 16진수 값

print(int(0b1010101010))    # 682

### 출력 연산자 : print() - 화면에 값들을 출력하는 함수
# print()는 하나의 값만을 출력하지 않고, 다수의 값을 출력할 수 있음. 구분자 ","를 이용함
print('a',1,1.1,True)
# sep 인자값은 여려개의 값을 구분할 때에 사용할 값을 지정할 수 있다. 기본값은 ' '으로 여백
print('a',1,1.1,True,sep='-')
# end 인자값은 출력 결과의 끝에 들어갈 값을 지정할 수 있다. 기본값은 "\n"
print(1)
print(2)
print(3,end=' ')
print(4)

''' print()를 이용하여 다음과 같이 만들어 보세요
    이때에 print()사용할 때에 escape문자를 사용하세요.
(결과)
            #### 회비 정보 ####
================================================
이름      나이      전화번호        회비
================================================
김동완    38      010-1111-1111     ￦20,000
서지수    24      010-1234-5678     ￦30,000
이지은    25      010-2525-2345     ￦50,000
------------------------------------------------
총합계                              ￦100,000
================================================
'''

print("\t\t","#"*4,"회비 정보", "#"*4)
print("="*50)
print('이름\t나이\t  전화번호\t\t회비')
print("="*50)
print('김동완\t38\t010-1111-1111\t\t￦20,000')
print('서지수\t24\t010-1234-5678\t\t￦30,000')
print('이지은\t25\t010-2525-2345\t\t￦50,000')
print("-"*50)
print('총합계\t\t\t\t\t￦100,000')
print("="*50)

print("\t\t","#"*4,"회비 정보", "#"*4,"\n",
      "="*50,
      '\n김동완\t38\t010-1111-1111\t\t￦20,000',
      '\n서지수\t24\t010-1234-5678\t\t￦30,000', 
      '\n이지은\t25\t010-2525-2345\t\t￦50,000\n',
      "-"*50,"\n",
      '총합계\t\t\t\t\t￦100,000\n',
      "="*50)
"""
## 서식문자
#
#   c스타일        파이썬3      설명
#   %s              {}          문자열 출력
#   %d              {}          정수 출력
#                   {:b}        표현식(0b) 없는 2진수 값 출력
#   %o              {:o}        표현식(0o) 없는 8진수 값 출력
#   %x              {:x}        표현식(0x) 없는 16진수 값 출력
#   %f              {:f}        실수 출력
#   %.2f            {:2f}       소수점 2자리까지의 실수 출력
#   %6d             {:6}        6자리 고정 출력

# 문자열 정수 출력
print("%s님의 나이는 %d 입니다." % ('김동완',38))
print("{}님의 나이는 {} 입니다.".format('김동완',38))

# 문자열 실수 출력
print("%s님의 무게는 %f 입니다." % ('김동완',75.5))
print("{}님의 무게는 {:f} 입니다.".format('김동완',75.5))

# 고정길이 출력
print("원주율 = %8.3f" % (3.141592))
print("원주율 = {:8.3f}".format(3.141592))

# 정렬하여 출력
print("%10s" % ('오른쪽'))
print("%-10s" % ('왼쪽'))
print("{:>10},{:<10}".format('오른쪽','왼쪽'))
print("{:^10}".format('가운데'))

# 빈 여백을 채워서 출력
print("%5d %05d" %(1,1))
print("{:5} {:05}".format(1,1))
# 문자열의 경우네는 정렬 후 여백에 사용할 문자를 ":"다음에 입력
print("{:_>10}".format('test'))
print("{:_^10}".format('test'))
print("{:_<10}".format('test'))

# 천단위 구분 출력
print("{:,}".format(100000000))

# 문제
print("{: ^50}".format('파이썬 쇼핑몰'))
print('번호 : {}'.format(1078718855))
print('주소 : {}'.format('서울시 종로구 종로3가'))
print('성명 : {}'.format('김사장'))
print('전화 : {}'.format('070-1234-5678'))
print("{}".format('-'*50))
print("{: ^20}{: ^5}{: ^10}{: ^10}".format('품명','단가','수량','금액'))
print("{}".format('-'*50))
print("{: ^15}{:,}{: ^15}{:,}".format('블루투스 이어폰',85000,'1',85000))
print("{: ^20}  {:,} {: ^15} {:,}".format('USB3.0 8G',8000,'1',8000))
print("{}".format('-'*50))
print("{:<41}{:,}".format('소 계',93000))
print("{}".format('-'*50))
print("{:<39}{:,}".format('청구금액',93000))
print("{:<38}{:,}".format('받은금액',100000))
print("{:<40}{:,}".format('거스름돈',7000))
print("{}".format('-'*50))