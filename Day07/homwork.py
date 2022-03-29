# 2장 4번문제
word1 = input("첫번째 단어 : ")
word2 = input("두번째 단어 : ")
word3 = input("세번째 단어 : ")
print("="*20)
abbr = word1[0] + word2[0] + word3[0]
print("약자 : ",abbr)

# 3장 1번 A형문제
kg = int(input("짐의 무게는 얼마입니까? : "))
if kg < 10:
    print("수수료는 없습니다.")
else:
    print("수수료는 10,000원 입니다.")
    
# 3장 1번 B형문제
kg = int(input("짐의 무게는 얼마입니까? : "))
if kg < 10:
    print("수수료는 없습니다.")
else:
    print("수수료는 {:,}원 입니다.".format(10000*(kg//10)))
    
# 3장 2번문제
import random

print('>>숫자 맞추기 게임<<')
com = random.randint(1, 10) # 1 ~ 10 사이 난수 정수 발생

while True:
    my = int(input("예상 숫자를 입력하시오 : "))    # 숫자 입력
    if my < com:
        print("큰 수 입력")
    elif my > com:
        print("작은 수 입력")
    else:
        print("~~성공~~")
        break
# 3장 3번 문제 
print("수열 = ",end=' ')
Sum = 0
for i in range(1,100):
    if i % 3 == 0 and i % 2 != 0:
        print(i,end=' ')
        Sum += i
print()
print("누적합 : ",Sum)

# 3장 4번 문제
multiline="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
count = 0
word = multiline.split()
for i in range(len(word)):
    count += 1
    print(word[i],end='\n')
print("단어 개수 : ",count)

# 4장 1번 문제
lst = [10, 1, 5, 2]
result = lst+lst
print("단계 1 : ",result)
lst2 = lst[0] * 2
result.append(lst2)
print("단계 2 : ",result)
result2 = []
for i in range(len(result)):
    if i % 2 != 0:
        result2.append(result[i])
print("단계 3 : ",result2)

# 4장 2번 문제 A형
lst = []
num = int(input("vector 수 : "))

for i in range(num):
    lst.append(input("입력 : "))
print("vector 크기 : ",len(lst))

# 4장 2번 문제 B형
lst = []
num = int(input("vector 수 : "))

for i in range(num):
    lst.append(input("입력 : "))

su = input("찾을 값 : ")
if su in lst:
    print("YES")
else:
    print("NO")

# 4장 3번 문제 A형
message = ['spam','ham','spam','ham','spam']   
dummy = [1 if i == 'spam' else 0 for i in message]    
print(dummy)

# 4장 3번 문제 B형
message = ['spam','ham','spam','ham','spam']
lst = [msg for msg in message if msg == 'spam']
print(lst)

# 4장 4번 문제
position = ['과장','부장','대리','사장','대리','과장']
print("중복되지 않은 직위 : ",set(position))

cnt = {}
position = ['과장','부장','대리','사장','대리','과장']
for i in position:
    cnt[i] = cnt.get(i,0)+1


print("각 직위별 빈도수 : ",cnt)