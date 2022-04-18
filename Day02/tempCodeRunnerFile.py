name = input("이름 : ")
height = float(input("키 : "))
kg = float(input("체중 : "))

std = (height - 100) * 0.9
fat = kg / std * 100

fatId = ""

if fat <= 100:
    fatId = "저체중"
elif fat > 100 and fat <= 110:
    fatId = "정상 체중"
elif fat > 110 and fat <= 120:
    fatId = "과체중"
elif fat > 120 and fat <= 130:
    fatId = "비만"
else:
    fatId = "고도비만"


print("{}님의 비만도는 {:.2f}% {}입니다.".format(name, fat, fatId))