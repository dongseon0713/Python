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
