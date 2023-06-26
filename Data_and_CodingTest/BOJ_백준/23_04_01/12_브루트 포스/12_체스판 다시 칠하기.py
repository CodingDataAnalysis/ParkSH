import sys
import copy

A = list(map(int,sys.stdin.readline().split()))
print(A[0])
print(max(A))

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다.
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

chess = []
for i in range(A[0]):
    b = list((sys.stdin.readline().rstrip()))
    print(b)
    chess.append(b)

chess_origin = copy.deepcopy(chess)
# 단순 무식하게 따라서 처음 1열 1행 부터 8행 8열씩 짤라가며해보자
minE = 0
cnt = 0
i,j = 0,0
res = []
print(len(b))

for i in range(A[0]-7):
    for j in range(A[1]-7):
        for k in range(i , i+7): # 열
            # 열
            for p in range(j, j+7): #행
                if chess[k][p] =='B' and chess[k][p] == chess[k+1][p]:
                    chess[k+1][p] = 'W'
                    cnt+=1
                    if chess[k][p+1] == chess[k][p]:
                        chess[k][p+1] = 'W'
                        cnt+=1
                elif chess[k][p] =='W' and chess[k][p] == chess[k+1][p]:
                    chess[k+1][p] = 'B'
                    cnt+=1
                    if chess[k][p+1] == chess[k][p]:
                        chess[k][p+1] = 'B'
                        cnt+=1

        res.append(cnt)

print(res)
#%%
