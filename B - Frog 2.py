# https://atcoder.jp/contests/dp/tasks/dp_b

n, k = map(int, input().split())
stones = list(map(int, input().split()))
dp = [float("-inf") for _ in range(n+1)]
# recursion 

def solve(n):
    if n == 0:
        return 0
    if dp[n] != float("-inf"):
        return dp[n]
    cost = float("inf")
    for i in range(1, k+1):
        if n-i >= 0:
            cost = min(cost, solve(n-i)+abs(stones[n]-stones[n-i]))
    dp[n] = cost
    return dp[n]

print(solve(n-1))


dp[0] = 0
# iterative 
def solve2(n):
    for i in range(n):
        cost = float("inf")
        for j in range(1, k+1):
            if i+j < n:
                cost = min(cost, dp[i] + abs(stones[i]-stones[i+j]))
            else:
                return dp[i+j-1]
                
        dp[i] = cost
    # return dp[i]
        
print(solve2(n))
            
        


