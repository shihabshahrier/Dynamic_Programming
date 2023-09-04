# https://atcoder.jp/contests/dp/tasks/dp_a
# LIMIT = 10**4+7
# dp = [float("inf") for _ in range(LIMIT)]
n = int(input())
dp = [float("inf") for _ in range(n+1)]
stones = list(map(int, input().split()))

# N = 4
# stones = [10, 30, 40, 20]

# recursion
def solve(n):
    if n <= 0:
        return 0
    if n == 1:
        return abs(stones[1] - stones[0])
        
    if dp[n] != float("inf"):
        return dp[n]
    j1 = abs(stones[n] -  stones[n-1]) + solve(n-1)

    j2 = abs(stones[n] -  stones[n-2]) + solve(n-2)
    print(j1, j2)
    dp[n] = min(j1, j2)
    return dp[n]
print(solve(n-1))


# iterative 
dp[0] = 0
if n == 0:
    print(0)
elif n>=1:
    dp[1] = abs(stones[1] - stones[0])
if n >= 2:
    for i in range(2, n):
        j1 = abs(stones[i] - stones[i-1]) + dp[i-1]
        j2 = abs(stones[i] - stones[i-2]) + dp[i-2]
        # print(j1, j2)
        dp[i] = min(j1, j2)

print(dp[n-1])
    

