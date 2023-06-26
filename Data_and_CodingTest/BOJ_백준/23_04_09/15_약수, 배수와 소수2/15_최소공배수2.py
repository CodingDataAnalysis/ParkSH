import sys
import math

A,B = list(map(int, sys.stdin.readline().split()))
print(A*B//math.gcd(A,B))
