# 문제 5장 1번
def StarCount(height):
    cnt = 0
    for i in range(height):
        for j in range(i+1):
            print("*",end='')
            cnt += 1
        print()
    return cnt    
height = int(input('height : '))
print('star 개수 : {}'.format(StarCount(height)))

# 문제 5장 2번
def bank_account(bal):
    balance = bal   
    
    def getBalance():
        return balance
    def deposit(money):
        nonlocal balance
        balance += money
    def withdraw(money):
        nonlocal balance
        if balance < money:
            print("잔액이 부족합니다.")
        else:
            balance -= money
        
    return getBalance,deposit,withdraw

bal = int(input("최초 계좌의 잔액을 입력하세요 : "))
getBalance,deposit,withdraw = bank_account(bal)

print("현재 계좌의 잔액은 {}원 입니다".format(getBalance()))
money = int(input("입금액을 입력하세요 : "))
deposit(money)
print("{}원 입금 후 잔액은 {}원 입니다.".format(money,getBalance()))
money = int(input("출금액을 입력하세요 : "))
withdraw(money)
print("{}원 출금 후 잔액은 {}원 입니다.".format(money,getBalance()))

# 5장 문제 3번
def Factorial(n):
    if n == 1 :
        return 1
    else:
        result = n * Factorial(n-1)
    return result

result_fact = Factorial(10)
print('팩토리얼 결과 : ',result_fact)

# 6장 문제 1번
class Rectangle:
    width = height = 0
    
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def area_calc(self):
        area = self.width * self.height
        return area
    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum
print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input('사각형의 가로 입력 : '))
h = int(input('사각형의 세로 입력 : '))
print('-'*50)
rectangle = Rectangle(w, h)
print('사각형의 넓이 : ',rectangle.area_calc())
print('사각형의 둘레 : ',rectangle.circum_calc())
print('-'*50)

# 6장 문제 2번
from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]

# 산포도 클래스
class Scattering:
    def __init__(self,x):
        self.x = x
        
    def var_fun(self):
        avg = mean(self.x)
        diff = [(d- avg) ** 2 for d in self.x]
        var = sum(diff) / (len(self.x) - 1)
        return var
    def std_func(self):
        avg = mean(self.x)
        diff = [(d- avg) ** 2 for d in self.x]
        var = sum(diff) / (len(self.x) - 1)
        sd = sqrt(var)
        return sd

s = Scattering(x)

print("분산 : ",s.var_fun())
print("표준편차 : ",s.std_func())

# 6장 문제 3번
class Person:
    age = 0
    name = None
    gender = None
    
    def __init__(self,age,name,gender):
        self.age = age
        self.name = name
        self.gender = gender
    
    def display(self):
        if self.gender == 'male':
            self.gender = '남자'
        elif self.gender == 'female':
            self.gender = '여자'
        else:
            print("성별 입력 오류")
        print("이름 : ",self.name,', 성별 : ',self.gender,'\n나이 : ',self.age)
        
name = input("이름 : ")
age = int(input('나이 : '))
gender = input('성별(male/female) : ')

p = Person(age, name, gender)

p.display()

# 6장 문제 4번

class Employee:
    name = None
    pay = 0
    
    def __init__(self,name):
        self.name = name
        
class Permanent(Employee):
    def __init__(self, money, bonus):
        super().__init__(name)
        self.pay = money + bonus

class Temporary(Employee):
    def __init__(self,time,timepay):
        super().__init__(name)
        self.pay = time * timepay

empType = input('고용형태 선택(정규직<P>, 임시적<T>) : ')
if empType == 'p' or empType == 'p':
    name = input("이름 : >? ")
    money = int(input("기본금 : >? "))
    bonus = int(input("상여금 : >? "))
    p = Permanent(money, bonus)
    print("고용형태 : 정규직")
    print("이름 : ",p.name)
    print("급여 : {:,}".format(p.pay))
elif empType == 'T' or empType == 't':
    name = input("이름 : >? ")
    time = int(input("작업시간 : >? "))
    timepay = int(input("시급 : >? "))
    p = Temporary(time, timepay)    
    print("고용형태 : 임시직")
    print("이름 : ",p.name)
    print("급여 : {:,}".format(p.pay))
else:
    print('='*30)
    print('입력 오류')