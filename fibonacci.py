LIMIT = 10**6

# dp = [float("-inf") for _ in range(LIMIT)]
dp = [float("-inf")]*LIMIT

def fibonacci(n):
    # Top Down
    if n == 1:
        return 1
    if n <= 0:
        return 0

    if dp[n] != float("-inf"):
        return dp[n] # Memoize
        
    else:
        x = fibonacci(n-1) + fibonacci(n-2)
        dp[n] = x
        return dp[n]

n = 5
print(fibonacci(n))

# Bottom up 
dp[0], dp[1] = 0, 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

        
    