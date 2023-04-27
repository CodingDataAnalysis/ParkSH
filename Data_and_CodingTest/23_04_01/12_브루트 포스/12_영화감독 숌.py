import sys

N = int(sys.stdin.readline())
movie = 666
while N:
    if "666" in str(movie):
        N -= 1
    movie += 1
    print(movie)

print(movie - 1)
# 0a ==> 1
# 1a ~ 9a ==> 9
# 10a 11a 12a 13a 14a 15a 1a1~1a9 17a 18a 19a==> 9+9
# 60a 61a 62a 63a 64a 65a a01~a99 67a 68a 69a==>9+9 + 90
# 90a ~ 99a ==> 9+9
# ==> 18*9 + 90 ==> 252

#100a ~ 500a
#600a~666a

#%%
