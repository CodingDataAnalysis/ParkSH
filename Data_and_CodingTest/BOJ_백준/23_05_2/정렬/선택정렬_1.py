import sys
from collections import deque

def selection_sort(A ,k) : # A[1..N]을 오름차순 정렬한다.

    i = len(A)-1
    b = deque()
    p = 0
    res = []
    while True:
        if i == 0:
            break

        A_idx = A.index(max(A[:i]))
        # print(f'max:{max(A[:i])}')
        # print(f'A[:i] : {A[:i]}')
        # print(f'A[i] : {A[i]}')
        if max(A[:i]) > A[i]:
            idx = A[i]
            # print(idx)
            A[i] = max(A[:i])
            b.appendleft(max(A[:i]))
            A[A_idx] = idx
            # print(f'A : {A}')
            # print('---')
            p+=1
            if p == k:
                res.append((idx,A[i]))
                res = res[0]
        else:
            # print('===')
            i-=1

    if p<k:
        return print(-1)
    else:
        return print(*res)



N,K = list(map(int,sys.stdin.readline().split()))

A = list(map(int,sys.stdin.readline().split()))
selection_sort(A,K)

#%%
