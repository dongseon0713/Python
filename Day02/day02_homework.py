## [문제1]
print('문제 1번')
su = 5
dan = 800
price = su * dan

print('su 주소 : ', id(su))
print('dan 주소 : ', id(dan))
print('금액 : ',price)

## [문제2]
print('문제 2번')
x = 2
y = 2.5 * x**2 + 3.3 * x + 6

print('2차 방정식 결과 : ', y)

## [문제3]
print('문제 3번')
fat = int(input("지방의 그램을 입력하세요 : "))
carbohydrate = int(input("탄수화물의 그램을 입력하세요 : "))
protein = int(input("단백질의 그램을 입력하세요. : "))
kcal = fat*9 + carbohydrate*4 + protein*4

print("총 칼로리 : {:,} cal".format(kcal))