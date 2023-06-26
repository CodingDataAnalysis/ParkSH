import sys

window= [[0,0,0,1],[0,0,2,0],[1,0,0,1],[0,2,0,0], [0,0,0,0]]
# [0,0,0] , [1,3] ,20

rain = [[2,3,2],[4,4,1],[1,2,5]]
k = 3

# window =[[0,0,0]]
# rain = [[1,3,15]]
# k=20]

# def solution(window , rain , k):
answer = 0
for sero, garo, width in rain:
    # print(sero)
    sero_idx = sero-1
    garo_idx = garo-1
    window[sero_idx][garo_idx] += width
    while True:
        if sero_idx >= len(window)-1:
            break

        if window[sero_idx][garo_idx]>=k:
            idx = window[sero_idx][garo_idx]
            window[sero_idx+1][garo_idx] += idx
        sero_idx+=1
    # print(window)
    if window[-1][garo_idx]>=k:
        answer += window[-1][garo_idx]
print(answer)
#     return 0
# solution(window, rain ,k)
#




#%%
