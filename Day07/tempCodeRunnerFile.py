cnt = {}
position = ['과장','부장','대리','사장','대리','과장']
for i in position:
    cnt[i] = cnt.get(i,0)+1


print("각 직위별 빈도수 : ",cnt)