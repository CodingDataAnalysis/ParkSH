import sys

def selection_sort(A ,k) : # A[1..N]을 오름차순 정렬한다.

    i = len(A)-1
    p = 0
    res = []
    while True:
        if i == 0:
            break
        if p>k:
            break
        A_idx = A.index(max(A[:i]))

        if max(A[:i]) > A[i]:
            idx = A[i]
            A[i] = max(A[:i])
            A[A_idx] = idx
            p+=1
            if p == k:
                res.append((idx,A[i]))
                res = res[0]
        else:
            i-=1

    if p<k:
        return print(-1)
    else:
        return print(*res)

N,K = list(map(int,sys.stdin.readline().split()))
A = list(map(int,sys.stdin.readline().split()))
selection_sort(A,K)

#%%
