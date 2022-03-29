num = 1    
word = input("단어를 입력하세요 : ")
for i in word:
    new_word = len(word) - num
    word1 = word[new_word]
    print(word1)
    num += 1