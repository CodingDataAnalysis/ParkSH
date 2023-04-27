import sys
import heapq

N = int(sys.stdin.readline())
res = []
for i in range(N):
    a = sys.stdin.readline().rstrip()
    heapq.heappush(res, (len(a), a))

res = list(set(res))  # 중복된 값을 제거하기 위해 set을 사용한 뒤 리스트로 변환합니다.
res.sort(key=lambda x: (x[0], x[1]))  # 단어 길이가 같은 경우 알파벳 순서로 정렬합니다.

for r in res:
    print(r[1])  # 정렬된 단어를 출력합니다.



#%%
