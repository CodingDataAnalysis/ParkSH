import sys


def hanoi(n, start, end, auxiliary):
    # n개의 원판을 start에서 end 로 옮기기
    if n == 1:
        print(start, end) # 재귀 종료 조건
    else:
        hanoi(n - 1, start, auxiliary, end)
        # n-1 개 원판을 시작 기둥에서 보조 기둥으로 이동
        # 목표 기둥은 임시로 사용하는 보조 기둥이 된다.
        print(start, end)
        # 현재 원판을 시작 기둥에서 목표 기둥으로 이동
        hanoi(n - 1, auxiliary, end, start)
        #n-1개의 원판을 보조 기둥에서 목표 기둥으로 이동

n = int(sys.stdin.readline())

# 이동 횟수인 2^n - 1을 출력
print(2 ** n - 1)

# 하노이 탑 이동 순서 출력
hanoi(n, 1, 3, 2)

# hanoi(3 , 1, 3, 2)

# ==> hanoi(2, 1 , 2, 3) ==> hanoi(1, 1,3,2) ==> print(1,3)
#                        ==> print(1,2)
#                        ==> hanoi(1,3,2,1) ==> print(3,2)
# ==> print(1, 3)
# ==> hanoi(2, 2 , 3 , 1) ==> hanoi(1,2,1,3) ==> print(2,1)
#                         ==> print(2,3)
#                         ==> hanoi(1,1,3,2) ==> print(1,3)




# 1 2 3

# 1
# 2
# 3

# 2
# 3    1

# 3  2 1

#    1
# 3  2

#    1
#    2  3

# 1  2  3

#       2
# 1     3

#       1
#       2
#       3
#%%
