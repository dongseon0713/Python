food = {}
for i in range(1,5):
    food.update({i:input("좋아하는 음식을 입력하세요 : ")})
print(food)
dele = int(input("제거하고 싶은 항목이 무엇입니까?(숫자 입력) : "))

food.pop(dele)

print(food)