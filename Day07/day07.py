## 함수(Function)
#   : 프로그램에서 사용할 기능을 미리 정의해서 구현한 것
#    (또 다른 의미의 프로그램 내에 작은 프로그램)
#
#  python의 함수 정의(생성)
#    def 함수이름([인자list])
#        함수기능에 대한 정의1
#        함수기능에 대한 정의2
#        함수기능에 대한 정의3
#        ...
#
#  - 함수 사용에 있어서 설명이 필요한 경우, 함수 내부에 주석을 사용하여 기술(여러줄주석)
#  - 함수를 만들 때에 함수의 기능을 바로 알 수 있는 이름으로 정의하길 권장함.
#  - 미리 만들어 놓은 함수를 호출 시에는, "함수이름([인자...])"로 호출
#  - 정의 생성된 함수의 반환값이 있는 경우, "return" 명령어를 사용.
#  - 함수에 반환값이 있을 수도 있고, 없을 수도 있다. 있는 경우 return을 사용
#    없는 경우에 "return"은 함수가 종료
#  - 함수에 필요하면 인자값을 전달할 수 있다. 전달된 인자값은 함수 정의시에 만든
#    "매개변수"에 그 값이 저장된다. 이후에 함수 정의부에서 해당 내용을 가지고 구동

# 예제 1] 사용자가 입력한 값을 출력하는 함수 구현
def pr():
    txt = input("입력 값 : ")
    print()
    print("입력한 내용은 : ",txt)
# 함수 호출
pr()

# 실습 - 입력값을 받아서 사칙연산하는 프로그램 함수를 사용.
#        그 함수의 이름은 calc()로 구현해 보세요.
#        (메인에서 calc()호출하면 모든 동작이 가능하도록 설정)


def calc():
    import os
    while True:
        os.system("cls")
        calc = input("계산할 수식을 입력하세요[ex) 5+5] : ")
        if '+' in calc:
            num1 , num2 = calc.split('+')
            num1 = int(num1)
            num2 = int(num2)
            print("계산 결과 : ",num1 + num2)
        elif '-' in calc:
            num1 , num2 = calc.split('-')
            num1 = int(num1)
            num2 = int(num2)
            print("계산 결과 : ",num1 - num2)
        elif '*' in calc:
            num1 , num2 = calc.split('*')
            num1 = int(num1)
            num2 = int(num2)
            print("계산 결과 : ",num1 * num2)
        elif '/' in calc:
            num1 , num2 = calc.split('/')
            num1 = int(num1)
            num2 = int(num2)
            print("계산 결과 : ",num1 / num2)
        else:
            print("수식입력이 잘못 되었습니다. \n다시 입력해주세요 !!!")
        sel = input("계속 하겠습니까??(Y/n) : ")
        if sel == 'n':
            break
    print("계산기 프로그램을 종료합니다.!!!")
    
calc()


# 예제 2] 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수 구현
#         사용자로부터 입력받은 값을 인자값으로 처리하는 함수.

# 함수 정의
def pr2(str1):
    print("입력한 내용은 : ",str1)
    
# 메인
txt = input("입력 : ")
print()
pr2(txt)

# 실습 - 입력값 받아서 사칙연산하는 프로그램 함수를 사용하여 동작하게 만드세요.
#        함수 명은 "calc([문자열인자값])"로 사용하세요.

# 함수 정의
def calc(calc):
        if '+' in calc:
            num1 , num2 = calc.split('+')
            num1 = int(num1)
            num2 = int(num2)
            print("계산 결과 : ",num1 + num2)
        elif '-' in calc:
            num1 , num2 = calc.split('-')
            num1 = int(num1)
            num2 = int(num2)
            print("계산 결과 : ",num1 - num2)
        elif '*' in calc:
            num1 , num2 = calc.split('*')
            num1 = int(num1)
            num2 = int(num2)
            print("계산 결과 : ",num1 * num2)
        elif '/' in calc:
            num1 , num2 = calc.split('/')
            num1 = int(num1)
            num2 = int(num2)
            print("계산 결과 : ",num1 / num2)
        else:
            print("수식입력이 잘못 되었습니다. \n다시 입력해주세요 !!!")

# 메인  
import os
while True:
    os.system('cls') 
    txt = input("계산할 수식을 입력하세요[ex) 5+5] : ")
    clac(txt)       # 함수 호출
    sel = input("계속 하겠습니까??(Y/n) : ")
    if sel == 'n':
        break
print("계산기 프로그램을 종료합니다.!!!")

# 예제 3] 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수 구현
#         사용자로부터 입력 받은 값을 인자값으로 처리하는 함수
#         함수에 return을 사용하여 반환값을 처리하는 예제

# 함수 정의
def pr3(str1):
    """연산 결과 후에 반환값을 전달하는 함수"""
    return "입력한 문자열 : "+str1

# 메인
txt = input("입력 : ")
print()
pr_out = pr3(txt)
print(pr_out)

# 실습 ] 위의 내용을 토대로 계산 결과를 반환값으로 처리하는 함수로 변환\

# 함수 정의
def calc(calc):
        if '+' in calc:
            num1 , num2 = calc.split('+')
            num1 = int(num1)
            num2 = int(num2)
            return num1+num2
        elif '-' in calc:
            num1 , num2 = calc.split('-')
            num1 = int(num1)
            num2 = int(num2)
            return num1 - num2
        elif '*' in calc:
            num1 , num2 = calc.split('*')
            num1 = int(num1)
            num2 = int(num2)
            return num1 * num2
        elif '/' in calc:
            num1 , num2 = calc.split('/')
            num1 = int(num1)
            num2 = int(num2)
            return num1 / num2
        else:
            return 0

# 메인
import os
while True:
    os.system('cls') 
    txt = input("계산할 수식을 입력하세요[ex) 5+5] : ")
    result = calc(txt)       # 함수 호출
    if result:
        print("계산 결과는 : ",result)
    else:
        print("수식입력이 잘못 되었습니다. \n다시 입력해주세요 !!!")
    sel = input("계속 하겠습니까??(Y/n) : ")
    if sel == 'n':
        break
print("계산기 프로그램을 종료합니다.!!!")

# 두수에 대한 한번의 계산식을 입력받아서 결과를 출력하는 코드를 이용
# 다음과 같이 코딩을 해보세요!!
#   - 사용자가 계산식을 입력. 이것을 이용해서 처리
#   - calc()가 인자값으로 두 정수와 계산식(기초 : +,-,*,/)을 인자로 받아 처리하는
#     함수를 만들어 동작 시키세요.

def calc(num1,num2,giho):
        if '+' in giho:
            return num1+num2
        elif '-' in giho:
            return num1 - num2
        elif '*' in giho:
            return num1 * num2
        elif '/' in giho:
            return num1 / num2
        else:
            return 0

# 메인
import os
while True:
    os.system('cls') 
    txt = input("계산할 수식을 입력하세요[ex) 5+5] : ")
    if '+'in txt:
        su1,su2 = txt.split('+')
        su1 = int(su1); su2 = int(su2)
        giho = '+'
    elif '-'in txt:
        su1,su2 = txt.split('-')
        su1 = int(su1); su2 = int(su2)
        giho = '-'
    elif '*'in txt:
        su1,su2 = txt.split('*')
        su1 = int(su1); su2 = int(su2)
        giho = '*'
    elif '/'in txt:
        su1,su2 = txt.split('/')
        su1 = int(su1); su2 = int(su2)
        giho = '/'
    else:
        print("수식입력이 잘못됐습니다.\n다시 입력해주세요!!!")
        os.system('pause')
        continue
    result = calc(su1,su2,giho)     # 함수 호출
    if result != 0:     # 0인 경우는 수식이 잘못된 경우(+,-,*,/)
        if type(result) is not float:
            print("계산 결과는 : ".result)
        else:
            print("계산 결과는 : {:.2}".format(result))
    sel = input("계속하겠습니까?(Y/n) : ")
    if sel == 'n':
        break
print("계산 프로그램을 종료합니다!!")

## 함수 인자 기본값(default) 설정
#  default 이란? 입력 인자값이 없는 경우에 기본적으로 적용되어지는 값을 의미함.
#
#  형식)
#  def 함수이름(param1, param2=1)
#       함수정의문1
#       함수정의문2
#
#  이렇게 정의된 함수가 있는 경우, param2는 기본값으로 '1'을 가지고 있는 것임.
#  즉, 인자값으로 param2에 전달되지 않아도 기본값으로 '1'을 가진다.

# 예제 4] 함수 인자의 기본값 설정(인자1)
def pr4(par1=10):
    print(par1)
    
# 메인
pr4(10)
pr4(20)
pr4(3)
pr4()

# 인자를 2개 가진 경우(모두 default인 경우)
def pr5(par1=10,par2=20):
    print(par1,par2)

# 메인
pr5(100,200)        # 100 200
pr5(100)            # 100 20
pr5(200)            # 200 20
pr5()               # 10 20

# 인자가 2개이상, 기본값 1인 경우
def pr6(par1,par2=20):
    print(par1,par2)
    
# 메인
pr6(100,200)        # 100 200
pr6(100)            # 100 20 
pr6(200)            # 200 20
# pr6()               # TypeError: pr6() missing 1 required positional argument: 'par1'

# 인자의 기본값이 맨 앞에 있는 경우....
# def pr7(par1=10,par2):  # SyntaxError: 기본값 뒤에는 일반 인자가 존재 x
#    print(par1,par2)
    
# [Quiz]
# 1. 짝, 홀수를 구분하는 함수를 작성해 주세요.
def num(num1):
    if num1 % 2 == 0:
        return '짝수'
    else:
        return '홀수'

# 메인
su = int(input("숫자를 입력하세요 : "))
result = num(su)
print(result)
# 2. "3"의 배수를 판별하는 함수를 작성해 주세요.
def num(num1):
    if num1 % 3 == 0:
        print("3의 배수입니다.")
    else:
        print("3의 배수가 아닙니다.")

# 메인
num1 = int(input("숫자를 입력하세요 : "))
num(num1) 

# or
def multi(num):
    if not num%3:
        return True
    else:
        return False
    
# 메인
su2 = int(input("정수 입력 : "))
if multi(su2):
    print("3의 배수입니다")
else:
    print("3의 배수가 아닙니다.")
    
# 3. 계산기를 입력,출력,연산기능으로 나눠서 실행되게 작성해 주세요.
# 입력 => 계산 처리 => 출력
def calc(num1,num2,giho):
    if giho == '+':
        return num1+num2
    elif giho == '-':
        return num1-num2
    elif giho == '*':
        return num1*num2
    elif giho == '/':
        return num1/num2

def Output(num1,num2,giho,result):
    print(num1,giho,num2,"=",result)
    
def Input():
    num1,giho,num2 = int(input("첫번째 정수 입력 : ")) \
        , input("계산 기호 입력(+, -, *, /) : ") \
            , int(input("두번째 정수 입력 : "))
    resutl = calc(num1, num2, giho)
    Output(num1, num2, giho, result)
    
# 메인
Input()

# 4. 거꾸로 수를 반환하는 함수를 계산, 출력
#    기능으로 나눠서 작성해 주세요.
#    예) 123 => 321

def reverseCode(result):
    tmp, su = 0,0
    while True:
        tmp = result%10
        result = result // 10
        su = (su + tmp) * 10
        if not result :
            return su // 10

def display():
    result, su = 0,0
    result = int(input("정수 입력 : "))
    su = reverseCode(result)
    print("변환 전 값 : {}, 변환 후 값 : {}".format(result,su))
    
# 메인
display()

# 5. 예제 친구이름 관리를 함수로 기능을 나눠서 작성해주세요.
def showFr(lst):
    print(lst)
    
def addFr(lst):
    name = input("이름을 입력하세요 : ")
    lst.append(name)

def delFr(lst):
    name = input("이름을 입력하세요 : ")
    if name in lst:
        lst.remove(name)
        return True
    else:
        return False
    
def updaFr(lst):
    name = input("이름을 입력하시오 : ")
    if name in lst:
        a = lst.index(name)
        name1 = input("변경할 이름을 입력하세요 : ")
        lst[a] = name1     
        return True 
    else:
        return False
    
# 메인
import os
lst = []

while True:
    os.system("cls")
    print("--------------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("0. 종료")
    print("--------------------------")
    num = input("메뉴를 선택하세요 : ")
    if num == '1':
        showFr(lst)
        os.system('pause')
    elif num == '2':
        result = addFr(lst)
        if result:
            print("추가 성공")
        else:
            print("추가 실패")
        os.system('pause')
    elif num == '3':
        result = delFr(lst)
        if result:
            print("삭제 성공")
        else:
            print("삭제 실패")
        os.system('pause')
    elif num == '4':
        result = updaFr(lst)
        if result:
            print("수정 성공")
        else:
            print("수정 실패")
        os.system('pause')
    elif num == '0':
        print("프로그램을 종료합니다!!!")
        break
    else:
        print("잘못 입력하셨습니다.")
        print("다시 입력하세요")
        os.system('pause')
    
# or
def fr_llst(lst):    # 친구 목록 보기
    print("="*15,"친구목록보기","="*15)
    if lst != []:
        for i in range(len(lst)):
            print(f"{i} : {lst[i]}")
        else:
            print("등록된 친구가 없습니다.")

def fr_add(lst):    # 친구 목록 추가
    name = input("추가할 친구 이름을 추가하세요 : ")
    lst.append(name)
    
def fr_del(lst):    # 친구 목록 삭제
    name = input("삭제할 친구 이름을 입력하세요 : ")
    if name in lst:
        lst.remove(name)
    else:
        print("삭제할 친구가 없습니다.")
        
def fr_mod(lst):    # 친구 목록 수정
    name = input("수정할 친구 이름 입력하세요 : ")
    if name in lst:
        idx = lst.nadex(name)
    else:
        print("수정할 친구가 없습니다.")
        return
    name_mod = input("수정할 이름을 입력하세요 : ")
    lst[idx] = name_mod
    
# 메인
import os
lst = []

while True:
    os.system("cls")
    print("--------------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("0. 종료")
    print("--------------------------")
    sel = input("메뉴를 선택해주세요[0~4] : ")
    if sel == '1':
        fr_llst(lst)
        os.system('pause')
    elif sel == '2':
        fr_add(lst)
        os.system('pause')
    elif sel == '3':
        fr_del(lst)
        os.system('pause')
    elif sel == '4':
        fr_mod(lst)
        os.system('pause')
    elif sel == '0':
        print("프로그램을 종료합니다!!!")
        break
    else:
        print("메뉴 선택이 잘못됐습니다.")
        print("다시 입력하세요")
        os.system('pause')
            
# 문제) 알바 시급 프로그램 작성 (default 인자값 사용)
def pay(money=8500,day=8,month=30):
    return money*day*month

print("<<시급 계산 프로그램>>")
print("1. 기본급")
print("2. 일한 날짜 입력")
num = input("번호 입력 >> ")
if num == '1':
    result = pay()
    print("급여 : {:,}원".format(result))
elif num == '2':
    su = int(input("일한 날짜 입력 : "))
    result2 = pay(8500,8,su)
    print("급여 : {:,}원".format(result2))
    
# or
def alba(day=30):
    time = 8; price = 8500
    re = time * price * day
    return re

def display():
    num = input("<<시급 계산 프로그램>>\n1. 기본 급\n2. 일한 날짜 입력\n번호 입력 >> ")
    if num == '1':
        result = alba()
    elif num == '2':
        day = int(("일한 날짜 입력 : "))
        result = alba(day)
    print("당신의 급여는 : {:,}원 입니다.".format(result))   
    
# 메인
display()
    
## 인자값 처리 방식1 => 연속된 자료를 처리하는 함수의 인자 처리 방식

# 예제
def pr8(a,b,c):
    print(a,b,c)

# 메인
pr8(10,20,30)   # 10 20 30

# "*"를 이용하여 리스트 또는 튜플과 같은 자료를 연속된 인자의 값으로 처리
# 리스트 또는 튜플의 변수값을 받아서 "unpacking"하는 방식으로 인자를 전달
x = [100,200,300]
y = [10,20]
z = 1,2,3,4

pr8(*x)         # a, b, c = [100,200,300]  => *사용

pr8(*y,30)
# pr8(*z)       # TypeError

# "*"를 이용하여 연속된 자료(리스트, 튜플)에 데이터를 인자로 전달이 가능하나
# 인자의 개수와 전달되는 자료의 개수는 같아야 한다.(**)

# 인자값 처리 방식2 => 가변 인자 값 처리...
# - 고정인자 => 인자값을 반드시 정해진 값으로 1:1 로 인자를 전해야하는 인자(일반)
# - 가변인자 => 인자값을 정해진 개수로 전달하지 않고, 가변적으로 전달 가능한 인자
#
# 가변인자 설정은 함수 정의시에 매개변수(인자) 앞에 "*"를 사용한다.

# 전달된 인자 값들의 합을 구하는 예제
def sum_func(*par):
    result = 0
    print(par,type(par))    # 전달된 인자값 처리
    for su in par:
        result += su
    return result

def display():
    Sum = 0
    Sum = sum_func()
    print(Sum)
    Sum = sum_func(10,20,30)
    print("인자가 세개(10,20,30)인 경우 결과 : ",Sum)
    Sum = sum_func(10,20,30,40,50)
    print("인자가 다섯개(10,20,30,40,50)인 경우 결과 : ",Sum)
    
# 메인
display()

# 주의) 인자값 처리함에 있어 고정인자와 가변인자를 동시에 사용하는 경우,
# 고정인자를 먼저 처리하도록 한다. 즉, 가변인자는 마지막에 사용되게 해야 한다.

# "**"를 사용하는 경우는 딕셔너리에 대한 packing을 시도한다는 의미로 처리
#
# 예제) 딕셔너리 자료형을 받아서 처리하는 함수
def dic_func(**par):
    print(par,type(par))
    for k in par:
        print("{}:{}".format(k,par[k]))
        
# 메인
dic_func(피카츄='1마리',파이리='2마리',꼬부기='없음',라이칸='1')

dic = {
    'sep' : '-',
    'end' : '\n\n'
}

lst = ['test1','test2','test3','test4']

print('test','test',**dic)
print('test','test',sep='-',end='\n\n')
print(*lst,**dic)

    