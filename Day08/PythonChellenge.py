first_name = input("이름을 입력하세요 : ")
print(len(first_name))
last_name = input("성을 입력하세요 : ")
print(len(last_name))
name = last_name+" "+first_name
print(name)
print(len(name))

subject = input("가장 좋아하는 과목 이름을 입력하세요 : ")
print(subject+"-")

poem = "뾰족한 연필이 깨끗한 선을 그린다."
print(poem)
start_idx = int(input("시작인덱스를 입력하세요 : "))
last_idx = int(input("마지막 인덱스를 입력하세요 : "))

print(poem[start_idx:last_idx])

while True:
    str1 = input("대문자로 메시지를 입력하세요 : ")
    if str1 == str1.upper():
        break
    else:
        print("다시 입력하세요 !!")
        
str2 = input("영어 단어를 입력하세요 : ")
str3 = str2[0:2]
print(str3.upper())

name = input("이름을 입력하세요 : ")
count = 0
name = name.lower()

for i in name:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count +=1
print("모음의 개수 : ",count)

pw = input("비밀번호를 입력하세요 : ")
pw_ck = input("비밀번호를 한 번 더 입력하세요 : ")

if pw == pw_ck:
    print("Thank you")
elif pw.lower() == pw_ck.lower():
    print("They must be in the same case")
else:
    print("Incorrect")

num = 1    
word = input("단어를 입력하세요 : ")
for i in word:
    new_word = len(word) - num
    word1 = word[new_word]
    print(word1)
    num += 1