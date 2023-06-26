import sys
from collections import deque


while True:
    a = (str(sys.stdin.readline().rstrip()))
    if a=='.':
        break
    stt = ''
    for i in a:

        if i == '(' or  i==']' or i=='[' or i==')':
            stt +=i
    # print(stt)
    while True:
        if '[]' in stt:
            stt = stt.split('[]')
            stt = "".join(map(str , stt))
            # print(stt)
        elif '()' in stt:
            stt = stt.split('()')
            stt = "".join(map(str , stt))
            # print(stt)
        else:
            break
    if len(stt)>=1:
        print('no')
    else:
        print('yes')

#%%
