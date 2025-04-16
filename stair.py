def climb_stair(A):
    N = len(A)
    if N == 1:
        return A[0]

    dp = [0] * N

    dp[0] = A[0]
    dp[1] = A[1] + dp[0]

    for i in range(2, N):
        dp[i] = A[i] + min(dp[i - 1], dp[i - 2])

    return dp[N - 1]

print(climb_stair([10,15,20,5]))
