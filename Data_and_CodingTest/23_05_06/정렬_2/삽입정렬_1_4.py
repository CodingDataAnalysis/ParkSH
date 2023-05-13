# 입력 받기
import sys

n , t = list(map(int , sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

# 삽입 정렬 구현

def insertion_sort(arr , n,t):
    answer = -1
    k = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            if k==t:
                answer = arr[j+1]
                k+=1
                return answer
            j -= 1
            k+=1

        if k==t:
            answer = key
            return answer
        k+=1
        arr[j + 1] = key
    return answer


print(insertion_sort(arr,n,t))


#%%
