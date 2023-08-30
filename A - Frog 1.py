# https://atcoder.jp/contests/dp/tasks/dp_a
LIMIT = 10**6
dp = [float("inf") for _ in range(LIMIT)]
# n = int(input())
# stones = list(map(int, input.split()))

N = 4
stones = [10, 30, 40, 20]


def solve(n):
    if n == 0:
        return 0
    if dp[n] != float("inf"):
        return dp[n]

    cost = float("inf")
    cost = min(cost, abs(stones[n] -  stones[n-1]) + solve(n-1))
    if n > 1:
        cost = min(cost, abs(stones[n] -  stones[n-2]) + solve(n-2))
    dp[n] = cost
    return dp[n]


print(solve(N-1))

