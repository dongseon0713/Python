dic = {'a':1,'b':2,'c':3}
print(dic['c'])
dic['c'] = 5*dic['b']
print(dic['c'])
dic['d'] = 100
print(dic)

# 예제 2] 딕셔너리에 for문을 사용하는 경우
for k in dic:   #  딕셔너리 자료형을 이용한 for문에서는 변수는 "key"값을 저장!!
    print(k)
    print("키값 : {}, 키를 이용한 참조값 : {}".format(k,dic[k]))