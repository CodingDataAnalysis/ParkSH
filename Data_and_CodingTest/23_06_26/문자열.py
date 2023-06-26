from collections import deque
import time

start_time = time.time()




a = 'EUVersusUAEOnSoccerRN'
answer = ''
# print(ord('A'))
# print(ord('Z'))
cap = [i for i in range(65, 91)]

# queue = deque()
b = list(a)
print(b)
list_1 = list(map(lambda x : x if ord(x) in cap else '1' , b))
print(list_1)

list_2 = ''.join(list_1)
list_2 = (list_2.split('1'))
list_3 = list(filter(lambda x :  list_2 if x != '' else '' , list_2))
print(list_3)

for i in list_3:
    if len(i)<=2:
        answer+= i[0]
    else:
        answer+=i[0]
        answer+=i[-1]

print(answer)

end_time = time.time()

print('time : ', end_time-start_time)

#%%
