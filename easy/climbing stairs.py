def climbStairs(n):
    if n == 1 or n == 0:
        return 1
    return climbStairs(n-1) + climbStairs(n-2)

def climbStairs(self, n: int) -> int:
    memo = {}
    memo[0], memo[1] = 0, 1
    for i in range(2, n+2):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n+1]

print(climbStairs(38))