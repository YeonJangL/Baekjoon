N = int(input())
list = []

for i in range(N):
    x, y = map(int, input().split())
    list.append((x, y))

for i in range(N):
    cnt = 1
    for j in range(N):
        if (list[i][0] < list[j][0] and list[i][1] < list[j][1]):
            cnt += 1
    print(cnt, end = " ")
