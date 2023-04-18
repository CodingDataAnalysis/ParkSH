import sys
import math

N = int(sys.stdin.readline())
print(int(math.sqrt(N)))

# 1 ==> (1) ==> 1
# 2 ==> (1,0) ==>1
# 3 ==> (1,0,0) ==>1
# 4 ==> (1,0,0,1) ==>2
# 5 ==> (1,0,0,1,0) ==> 2
# 6 ==> (1,0,0,1,0,0) ==>2
# 7 ==> (1,0,0,1,0,0,0) ==> 2
# 8 ==> (1,0,0,1,0,0,0,0) ==> 3
# 9 ==> (1,0,0,1,0,0,0,1,1) ==> 4
# 10 ==>(1,0,0,1,0,0,0,1,1,1) ==> 5
# (1,1,1,1,1,1,1,1,1,1) 1

# (1,0,1,0,1,0,1,0,1,0) 2

# (1,0,0,0,1,1,1,0,0,0) 3

# (1,0,0,1,1,1,1,1,0,0) 4

# (1,0,0,1,0,1,1,0,0,1) 5

# (1,0,0,1,0,0,1,0,0,1) 6

# (1,0,0,1,0,0,0,0,0,1) 7

# (1,0,0,1,0,0,0,1,0,1) 8

# (1,0,0,1,0,0,0,1,1,1) 9

# (1,0,0,1,0,0,0,1,1,0) 10



#%%
