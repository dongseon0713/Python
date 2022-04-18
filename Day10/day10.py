# 객채지향 프로그래밍
# 1. 클래스와 오브젝트(객채)
#
# 클래스란? - 특정 대상을 지정하여 정의를 담고있는 것
#  - 실세계의 것을 모델링하여 속성(Attrebute, 맴버변수)와 동작(Method)를 갖는 데이터타입
#  - python에서 string, int, list, dict ... 모두다 클래스로 존재
#  - 예로 학생이라는 클래스를 생성한다면, 학생을 나타내는 속성과 학생이 행하는 행동을 함께
#    정의할 수 있음.
#  - 즉, 다루고자하는 데이터와 데이터의 연산을 하나로 캡슐화하여 클래스로 표현 가능
#  - 모델링에서 종요시하는 속성에 따라서 클래스의 속성과 행동이 달라짐.
#  

a = [1,2,3,4,5]     # list -> class
# print(help(a))
a.append('a')
print(a)

# 객체(object) - 클래스에 정의된 대로 개별적으로 구성되서 개별, 독립적인 대상을 의미
#  - 클래스로 생성되어 구체화 된 내용(객체 - 인스턴스)
#  - 파이썬은 모든 것(int, float str, list, dict ... etc)인 객체(인스턴스)
#  - 실제로 class가 인스턴스화 되어 메모리에 상주하고 있는 상태를 의미
#  - class가 빵틀(설계도)등이라면, object(객체)는 실제로 빵틀에 찍어낸 빵을 의미함.

## Class 선언하기
# 객체를 생성하기 위해서는 객체의 모체가 되는 class를 미리 선언해야 한다.
#
# (형식)
# class [클래스명]:
#       변수 선언 (맴버변수-속성)
#       def 생성자(인수):
#           명령문..
#       def 함수명(인수)
#           명령문..
#
# 예제 1]

# 클래스 선언
class Person:
    pass    # 클래스 정의 나중에 만들기 위해서 pass를 사용

# 객체 생성
bob = Person()
cathy = Person()

a = list()  # 빈 리스트 객체 생성
b = list()  # 빈 리스트 객체 생성

print(type(bob),id(bob))
print(type(cathy),id(cathy))
print(type(a),type(b))

## 클래스 생성자
#  - 생성자, 클래스 인스턴스가 생성될 때 호출됨
#  - __init__(self)가 기본으로 생성하게 된다. self가 인자로 처음에 오고, 이는 자신을 가리킴.
#  - 이름이 꼭 self인 필요는 없지만, 관례적으로 self로 사용
#  - 생성자는 해당 클래스에서 다루는 데이터를 정의할 수 있다.
#    정의하는 데이터를 맴버변수, 속성이라고 부름

class Person:
    def __init__(self):
        print(self,'is generated')
        self.name = '홍길동'        # 이름 속성
        self.age = 18               # 나이 속성

p1 = Person()
p2 = Person()

p1.name = '홍길자'
p1.age = 24

print(p1.name,p1.age)
print(p2.name,p2.age)

## 생성자에게 인자값을 전달하여 속성값을 부여하고 싶은 경우
class Person:
    def __init__(self,name,age=10):
        print(self,'is generated')
        self.name = name    # 이름 속성
        self.age = age      # 나이 속성

p1 = Person('bob',30)
p2 = Person('kate',20)
p3 = Person('홍길동')

print(p1.name,p1.age)
print(p2.name,p2.age)
print(p3.name,p3.age)

# 연습1]  Calc_class라는 클래스를 선언
#   속성 값은 x,y로 두개를 초기화 구현
#   생성자에서 x,y의 속성값을 받을 수 있게 생성
#   객체를 생성하여 해당 값을 참조해서 확인해 보세요
#

class Calc:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
p1 = Calc(10,20)
print(p1.x,p1.y)

## Method 정의
# 맴버함수라고도 부름. 해당 클래스의 object에서만 호출가능
# 메서드는 객체 레벨에서 호출되며, 해당 객체의 속성에 대한 연산을 행함
# 호출은 객체.매서드()형태로 호출됨.

class Calc_class:
    # 클래스 변수 : 속성
    x = y = 0
    
    # 생성자 : 객체 생성시 동작 + 맴버 변수 초기화
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # 클래스의 메서드(함수)
    def plus(self):
        p = self.x + self.y     # 맴버 변수 더하기 연산
        return p
    
    def minus(self):
        m = self.x - self.y
        return m
    
c = Calc_class(10, 20)
print(c.x,c.y,'더하기 연산 결과 : ',c.plus())
print(c.x,c.y,'빼기 연산 결과 : ',c.minus())

# 예제1] 자동차 클래스 생성
class Car:
    # 맴버 변수 선언
    cc = 0      # 엔진 cc
    door = 0    # 문짝 개수
    carType = None  # null
    
    # 생성자
    def __init__(self,cc,door,carType):
        # 맴버 변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType  # 승용차, suv, 경차
        
    def display(self):
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s입니다."%(self.cc,self.door,self.carType))
        
## 객체 생성
car1 = Car(2000, 4, "승용차")       # 객체 생성 + 초기 값
car2 = Car(3000, 4, "SUV")

car1.display()
car2.display()

## 소멸자(Destructor) : 생성자 반대 역할하는 소멸자는 __del__()이란 이름으로 제공
# 객체 사용이 완료되었을 떄에 자동으로 실행. 객체를 메모리에서 소멸시키는 역할을 한다.
#
# class muliply:
#       # 생성자
#       def __init__(self,x,y)
#           self.x = x
#           self.y = y
#
#       # 소멸자
#       def __del__(self)
#           del.self.x
#           del.self.y
#

## self
# 파이썬에서 Method는 항상 첫번째 인자로 self를 전달
# self는 현재 해당 메서드가 호출되는 객체 자신을 가리킴
# C++/C#, Java에서는 이를 this에 해당
# 이름이 꼭 self일 필요는 없으나, 관례상 self를 사용한다.
#

# 예시1]
class Person:
    name = None
    age = 0
    # 생성자
    def __init__(self,name,age):
        print("self : ",self)
        self.name = name
        self.age = age
        
    def sleep(self):
        print(self.name,"은 잠을 잡니다")
        
a = Person('Abram', 100)
b = Person('홍길동',18)

print(a)
a.sleep()
b.sleep()
b.age = 110
print(b.age)
print(a.age)

# Method 타입
#  - instance method : 객체로 호출
#       매서드는 객체 레벨로 호출되기 떄문에, 해당 매서드는 호출한 객체에만 영향을 미침
#  - class method : class로 호출
#       클래스 메서드의 경우, 클래스 레벨로 호출되기 때문에 클래스 맴버 변수만 변경 가능
# 

class DatePro:
    # 맴버 변수 선언
    content = "날짜 처리 클래스"
    
    # 생성자
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    
    # 객체 매서드(instance method)
    def display(self):
        print('%d-%02d-%d'%(self.year,self.month,self.day))
        
    # 클래스 매서드(class method) : 객체로 접근하는게 아니라 클래스로 접근하기 떄문에 self를 쓸 수 없다
    @classmethod # 함수 장식자
    def date_string(cls,dataStr):       # dataStr의 데이터는 '20020330'
        year = dataStr[0:4]
        month = dataStr[4:6]
        day = dataStr[6:]
        
        print(f"{year}년 {month}월 {day}일")

# 객체 맴버
date = DatePro(2022, 3, 30)     # 생성자

print(date.content)             # 날짜 처리 클래스
print(date.year)                # 2022
date.display()                  # 2022-3-30

# 클래스 맴버
print(DatePro.content)          # 날짜 처리 클래스
# print(DatePro.year)            # AttributeError 왜? 생성자에 의해서 생성되는 맴버변수
DatePro.date_string('20230330') # 2023년 03월 30일 

# 예제 2]
class Math:
    # 클래스 메서드 선언
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def mul(a,b):
        return a*b
    
print(Math.add(10, 20))
print(Math.mul(10, 20))

## 특수한 매서드
# - __로 시작하고, __로 끝나는 함수들은 특수 함수
# - 해당 메서드들을 구현하면, 커스텀 객체에 여러가지 파이썬 내장함수나 연산자를 적용 가능
# - 오버라이딩 가능한 함수 목록들은 https://docs.python.org/3/reference/datamodel.html에서 확인 가능
#

# 예시] Point클래스 - 2차원 좌표 평면에 각 점(x,y)
#       연산 -> 두 점의 덧셈, 뺼셈 (1,2) + (3,4) = (4,6)
#               한 점과 숫자의 곱셈 (1,2) * 3 = (3,6)
#       점의 길이는 (0,0)부터의 거리

class Point:
    # 초기 생성자
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    # 특수 메서드 호출 add
    def __add__(self, pt):
        new_x = self.x + pt.x
        new_y = self.y + pt.y
        return Point(new_x,new_y)
    
    def __mul__(self, pt):
        new_x = self.x * pt.x
        new_y = self.y * pt.y
        return Point(new_x,new_y)
    
    def __str__(self):
        return f"({self.x},{self.y})"
        
p1 = Point(3, 4)
p2 = Point(2, 7)

p3 = p1 + p2        # __add__
p4 = p1 * p2        # __mul__

print(p1)           # __str__
print(p2)
print(p3)
print(p4)

# 캡슐화 : 자료와 알고리즘이 구현된 함수를 하나로 묶고
#          공용 인터페이스 만으로 접근을 제한하여 객체의 세부 내용을 외부로부터 감추는 기법을 말함.

# 예제] 캡슐화
class Account:
    # 은닉 변수
    __balance = 0       # 잔액
    __accName = None    # 예금주
    __accNo = None      # 계좌번호
    
    # 생성자 : 맴버 변수 초기화
    def __init__(self,bal,name,no):
        self.__balance = bal    # 잔액
        self.__accName = name   # 예금주
        self.__accNo = no       # 계좌번호
        
    # Getter 계좌정보 확인
    def getBalance(self):
        return self.__balance, self.__accName,self.__accNo
    
    # Setter 입금하기
    def deposit(self, money):
        if money < 0:
            print("금액 확인")
            return              # 종료(exit)
        self.__balance += money
        
    def withdraw(self, money):
        if self.__balance < money:
            print("잔액 확인")
            return              # 종료(exit)
        self.__balance -= money
        
## 객체 생성(생성자로 초기값 설정)
acc = Account(10000, '홍길동', '123-123-3333-13')

## Getter : 예금 확인
# acc.__balance   # AttributeError
bal = acc.getBalance()
print("계좌 정보 : ",bal)

## Setter
acc.deposit(50000)      # 50,000원 입금
bal = acc.getBalance()
print("계좌 정보 : ",bal)

## Setter
acc.withdraw(10000)     # 10,000원 출금
bal = acc.getBalance()
print("계좌 정보 : ",bal)

## 클래스 상속(inheritance)
# 기준에 정의해둔 클래스의 기능을 그대로 물려받는 설정
# 기존 클래스에 기능 일부를 추가하거나, 변경하여 새로운 클래스를 정의
# 코드의 재사용
# 상속 받고자 하는 대상인 기존 클래스는 Parant, Super, Base 클래스라고 한다.
# 상속 받는 새로운 클래스 Child, Sub, Derived 클래스라고 한다.
# 의미적으로 is-a 관계를 갖는다.

# 예시] Person클래스를 선언하고, 자식으로 Student클래스를 선언
# 부모 클래스
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def eat(self, food):
        print(f"{self.name}은 {food}를 먹습니다.")
        
    def sleep(self, hour):
        print(f"{self.name}은 {hour}시간 동안 잡니다.")
    
    def work(self, minute):
        print(f"{self.name}은 {minute}분 동안 일합니다.")
    
 # 자식 클래스
class Student(Person):      # 부모 클래스에서 상속받는 경우 ()에 상속받는 클래스 지정
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def work(self, minute):
        print(f"{self.name}은 {minute}분 동안 공부합니다.")
        
class Employee(Person):
    pass

bob = Student('bob', 25)
bob.eat('초밥')
bob.sleep(1)
bob.work(60)

teacher = Employee('홍길동', 44)
teacher.eat('초밥')
teacher.work(11)

## Method override
# - 부모 클래스의 method를 재정의(override)
# - 자식 클래스(하위)의 인스턴스 호출시, 재정의된 매서드가 호출됨.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def eat(self, food):
        print(f"{self.name}은 {food}를 먹습니다.")
        
    def sleep(self, hour):
        print(f"{self.name}은 {hour}시간 동안 잡니다.")
    
    def work(self, minute):
        print(f"{self.name}은 {minute}분 동안 일합니다.")
    
 # 자식 클래스
class Student(Person):      # 부모 클래스에서 상속받는 경우 ()에 상속받는 클래스 지정
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def work(self, minute): # 부모 클래스의 매서드(work())를 기능 재정의 
        print(f"{self.name}은 {minute}분 동안 공부합니다.")
        
class Employee(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self, minute): # 부모 클래스의 기능을 재정의(work()) - method override
        print(f"{self.name}은 {minute}분 동안 업무를 진행합니다.")
        
bob = Student('bob', 25)
bob.eat('BBQ')
bob.sleep(8)
bob.work(360)

cathy = Employee('cathy', 35)
cathy.eat('초밥')
cathy.sleep(6)
cathy.work(480)

## super 클래스 : 하위 클래스(자식 클래스)에서 부모 클래스의 method호출할 때에 사용
# -> 자식 클래스 override하면 자식 클래스에서는 부모 클래스를 재정의 하면서
#    부모 매서드는 삭제가 됨. 이때에 부모 매서드를 가져오고 싶은 경우에 사용하는 것이 super이다.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def eat(self, food):
        print(f"{self.name}은 {food}를 먹습니다.")
        
    def sleep(self, hour):
        print(f"{self.name}은 {hour}시간 동안 잡니다.")
    
    def work(self, minute):
        print(f"{self.name}은 {minute}분 동안 일합니다.")
    
 # 자식 클래스
class Student(Person):      # 부모 클래스에서 상속받는 경우 ()에 상속받는 클래스 지정
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def work(self, minute):         # 부모 클래스의 매서드(work())를 기능 재정의
        super().work(minute)        # 부모 클래스의 work 매서드를 불러옴
        print(f"{self.name}은 {minute}분 동안 공부합니다.")
        
class Employee(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self, minute): # 부모 클래스의 기능을 재정의(work()) - method override
        print(f"{self.name}은 {minute}분 동안 업무를 진행합니다.")

bob = Student('bob', 25)
cathy = Employee('cathy', 35)
bob.work(60)
cathy.work(480)

# 기본적으로 상속은 기본 기능을 구현, 하위 재정의하거나 혹은 불러와 사용해야하는 경우
# override(재정의), super()을 이용하게 된다. 

# 예제] 
# 부모 클래스
class Parent:
    # 생성자
    def __init__(self,name,job):
        self.name = name
        self.job = job
        
    # 맴버 함수(매서드)
    def display(self):
        print('name : {}, job : {}'.format(self.name,self.job))

# 부모 클래스 객체 생성
p = Parent('홍길동', '회사원')
p.display()

# 자식 클래스
class Children(Parent):     # Parant클래스 상속 
    gender = None   # 자식 클래스의 맴버 변수 추가
    
    # 자식 클래스 생성자
    def __init__(self, name, job,gender):
        # 부모 클래스 생성자 호출
        super().__init__(name, job)
        self.gender = gender
        
    # 자식 클래스 맴버함수(method)
    def display(self):  # override(재정의)
        print('name : {}, job : {}, gender : {}'.format(self.name,self.job,self.gender))
        
# 자식 클래스 객체 생성
chil = Children('홍길숙', '의적자식', '여')
chil.display()

## 다형성 : 여러가지 형태를 가질 수 있는 능력을 의미함.
# -> 하나의 참조변수로 여러 타입(type)의 객체를 참조할 수 있는 것으로 정의
#   다형성은 상속관계에서 나올 수 있음. 

## 다형성 예제
# 부모 클래스
class Flight:
    
    # 부모 클래스 원형함수
    def fly(self):
        print("날다. fly 원한 메서드")
        
# 자식클래스 : 비행기
class Airplane(Flight):
    
    # 함수 재정의
    def fly(self):
        print("비행기 날다.")
        
# 자식클래스 : 새
class Bird(Flight):
    
    # 함수 재정의
    def fly(self):
        print("새가 날다")
        
# 자식클래스 : 종이비행기
class PaperAirplane(Flight):
    
    # 함수 재정의
    def fly(self):
        print("종이 비행기 날다.")
        
# 객체 생성
# 부모 객체 = 자식 객체 (자식1, 자식2)
flight = Flight()       # 부모 클래스 객체
air = Airplane()        # 자식 클래스 객체
bird = Bird()           # 자식 클래스 객체
paper = PaperAirplane() # 자식 클래스 객체

# 다형성
flight.fly()        # 날다. fly 원한 메서드

flight = air
flight.fly()        # 비행기 날다.

flight = bird
flight.fly()        # 새가 날다.

flight = paper
flight.fly()        # 종이 비행기 날다.

## 부모객체 참조 변수 = 자식객체 참조변수 방식으로 다형성을 할당할 수 있음.

## 내장 클래스 : builtins 모듈에 있는 클래스
lst = [1,2,3,4,5]
tuple = 1,2,3,4,5
dic = {1:'일',2:'이',3:'삼'}
dic2 = {'일':1,'이':2,'삼':3}
for i, c in enumerate(dic2):
    print("색인 : ",i, end=' ')
    print("내용 : ",c)
    
# 튜플 열거형 객체 이용
dic3 = {'name':'홍길동','job':'의적(도적)','addr':'서울시'}
for i, k in enumerate(dic3):
    print("순서 : ",i, end=' ')
    print("키 : ",k,end=' ')
    print("값 : ",dic3[k])
    
## ==================================================================
#### 시작점 만들기....(모듈)
# 모듈 안에 변수, 함수, 클래스 등을 포함할 수 있다. 이런 프로그램의 시작이 되는
# 시작점(main)을 만들 수 있다.
#
# (형식)
#  if __name__ == "__main__":   # 프로그램 시작점
#       명령문(메인에서 실행할 코드)
# 

# 연습 : 프로그램 시작점 만들기 예

# 1. 평균과 제곱근 모듈 import
from statistics import mean     # mean 평균
from math import sqrt           # sqrt 제곱근

# 2. 산술 평군
def Avg(data):
    avg = mean(data)
    return avg

# 3. 분산/표준편차 함수
def var_sd(data):   # [2,4,5,6,1,8] - avg
    avg = Avg(data) # 함수 호출
    diff = [(d - avg) **2 for d in data]    # list 내포
    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)
    return var, sd

## 프로그램 시작점 : 모듈을 불러오는 경우 메인인지 아닌지에 따라서 
## 실행여부를 결정함. 시작점 설정이 없으면 import시에 실행...
if __name__ == '__main__':
    data = [2,4,5,6,1,8]
    print("평균 : ",Avg(data))
    var ,sd = var_sd(data)
    print("분산 : ",var)
    print("표준 편차 : ",sd)
        
# ## 프로그램 시작점이 없는 경우
# data = [2,4,5,6,1,8]
# print("평균 : ",Avg(data))
# var ,sd = var_sd(data)
# print("분산 : ",var)
# print("표준 편차 : ",sd)