def jumpingOnClouds(n: int, c: list):
    i = jump = 0
    while i < n-1:
        i += 2
        if i != n and c[i] != 0:
            i -= 1
        jump += 1
    return jump
while 1:
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    print(jumpingOnClouds(n,c))