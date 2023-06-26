import sys

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr)+1)//2 # 분할 정복은 리스트를 정렬하는 알고리즘으로,
    # 1. 분할 : 정렬할 리스트를 절반으로 나눈다.
    # 2. 정복 : 각 부분 리스트를 재귀적으로 병합 정렬을 이용해 정렬한다.
    # 3. 결합 : 정렬된 부분 리스트들을 다시 하나의 정렬된 리스트로 병합한다.

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i,j = 0,0
    L2 = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L2.append(left[i])
            ans.append(left[i])
            i+=1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j+=1
    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i+=1
    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j+=1

    return L2

n, k = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
ans = []
merge_sort(a)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)

#%%
