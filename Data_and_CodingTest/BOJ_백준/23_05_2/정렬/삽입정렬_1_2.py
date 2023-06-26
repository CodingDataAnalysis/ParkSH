# 입력 받기
import sys

n , t = list(map(int , sys.stdin.readline().split()))
array = list(map(int, sys.stdin.readline().split()))

# 삽입 정렬 구현
k = 0
res = []
for i in range(n):
    # print(f'key : {key}')
    # 이전의 수 보다 타겟이 작아지는 것이 한 번 이라도 나타날 대 까지 루프
    for j in range(i,n-1):
        print(f'array : {array}')
        if array[j] > array[j+1]:
            array[j+1], array[j] = array[j], array[j+1]
        else:
            break

print(array)
#%%
