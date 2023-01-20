import sys
N, M = map(int, input().split())
K = [int(input()).split() for l in range(N)]
print(K)
a = [[int(c) for c in l.strip()] for l in sys.stdin]
