import sys
import copy

A = list(map(int ,sys.stdin.readline().split()))

B = []

# 10 13 ==>[0][0]~[7][7] , [0][1]~[7][8] ~~~ [7] [12] ==> 6번
#       ==>[1][0]~[8][7] , [1][1]~[8][8]~~~[8][12] ==> 6
#       ==>....[2][0]~[9][7] , ~~~ ==> 6개
# ==> 18개

res =[]
cnt = 0
for i in range(A[0]):
    B.append(list(sys.stdin.readline().rstrip()))
for a in range(A[0]-7): # 가로(행)
    for b in range(A[1]-7): # 세로(열)
        w_index = 0
        b_index = 0
        for i in range(a, a+8): # 8x8을 위해 8번 반복해야함 , 열(세로)
            for j in range(b, b+8): # 행(가로)
                if (i+j)%2==0:#짝수인 경우 ==> 첫번째 부터 실행
                    if B[i][j]!='W':#W가 아니면, 즉 B이면
                        w_index+=1#W로 칠하는 갯수
                    else:#W일 때
                        b_index+=1#B로 칠하는 갯수
                else:#홀수인 경우
                    if B[i][j]!='W':#W가 아니면, 즉 B이면
                        b_index+=1#B로 칠하는 갯수
                    else:
                        w_index+=1#W로 칠하는 갯수
        res.append(w_index)
        res.append(b_index)

print(res)

print(min(res))
#%%
