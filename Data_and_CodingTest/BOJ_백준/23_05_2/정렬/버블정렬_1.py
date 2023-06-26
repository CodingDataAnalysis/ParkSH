import sys

def bubble_sort(A,K):

    k = 0
    answer = -1
    for p in range(len(A)-1,0,-1):
        for i in range(p):
            if A[i] > A[i+1]:
                idx = A[i+1]
                A[i+1] = A[i]
                A[i] = idx
                k+=1
                if k==K:
                    answer = f'{A[i]} {A[i+1]}'

    return answer

A , K = list(map(int, sys.stdin.readline().split()))

N = list(map(int,sys.stdin.readline().split()))
print(bubble_sort(N,K))
