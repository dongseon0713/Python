# 챌린지 69
tu = ('korea','france','englend','spain','paris')
print(tu)
st = input("표시된 국가 이름들 중 하나를 입력하세요 : ")
if st == 'korea':
    print(tu.index('korea'))
elif st == 'france':
    print(tu.index('france'))
elif st == 'englend':
    print(tu.index('englend'))
elif st == 'spain':
    print(tu.index('spain'))
elif st == 'paris':
    print(tu.index('paris'))

# 챌린지 70
tu = ('korea','france','englend','spain','paris')
num = input("숫자를 입력하세요 : ")
if num == '0':
    print(tu[0])
elif num == '1':
    print(tu[1])
elif num == '2':
    print(tu[2])
elif num == '3':
    print(tu[3])
elif num == '4':
    print(tu[4])
else:
    print("숫자를 잘못 입력했습니다.")
    
# 챌린지 71
lst = ['축구','야구']
sports = input("좋아하는 스포츠는 무엇입니까? : ")
if sports in lst:
    lst.remove(sports)
    lst.append(sports)
    print(lst)
else:
    lst.append(sports)
    print(lst)
    
# 챌린지 72
subject = ['국어','영어','수학','과학','사회','체육']
print(subject)
name = input("좋아하지 않는 과목은 무엇입니까? : ")
if name in subject:
    subject.remove(name)
else:
    print("과목이 없습니다.")
print(subject)

# 챌린지 73
food = {}
for i in range(1,5):
    food.update({i:input("좋아하는 음식을 입력하세요 : ")})
print(food)
dele = int(input("제거하고 싶은 항목이 무엇입니까?(숫자 입력) : "))

food.pop(dele)

print(food)