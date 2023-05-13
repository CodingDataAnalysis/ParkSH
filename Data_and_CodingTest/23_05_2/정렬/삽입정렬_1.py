# 입력 받기
import sys

n , t = list(map(int , sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

# 삽입 정렬 구현
k = 0
res = []
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        res.append(arr[j+1])
        j -= 1
        # print(f'arr : {arr}')
        k+=1
    k+=1
    arr[j + 1] = key
    if k>=2:
        res.append(arr[j+1])
if len(res)<t:
    print(-1)
else:
    print(res[t-1])
# 결과 출력
# if k > n:
#     print("-1")
# else:
#     print(arr[k - 1])


# 4 5 1 3 2 ==> key 값 2번째 요소 5

# 4 5 5 3 2 ==> key값 보다 작은 3번째 요소 1값 대신 5로 채워 넣는다.

# 1 4 5 3 2

# 1 4 5 5 2

# 1 4 4 5 2

# 1 3 4 5 2

# 1 3 4 5 5

# 1 3 4 4 5
#%%
