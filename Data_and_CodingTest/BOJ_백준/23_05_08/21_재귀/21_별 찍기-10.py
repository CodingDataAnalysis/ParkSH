import sys

def draw_stars(n, x, y):
    if n == 1:
        stars[y][x] = "*"
        #
    else:
        size = n // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue  # 가운데 부분은 공백으로 남김
                draw_stars(size, x + size * i, y + size * j)

n = int(sys.stdin.readline())

# 출력할 별의 크기를 설정
stars = [[" "] * n for _ in range(n)]

draw_stars(n, 0, 0)

# 별 찍기 결과 출력
for row in stars:
    print("".join(row))

#%%
