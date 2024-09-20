def count_phone_numbers(N):
    dp = [[0 for i in range(10)] for i in range(N)]
 
    for i in range(10):
        if i != 8 and i != 0:
            dp[0][i] = 1

    for i in range(1, N):
        dp[i][0] = dp[i - 1][4] + dp[i - 1][6]
        dp[i][1] = dp[i - 1][6] + dp[i - 1][8]
        dp[i][2] = dp[i - 1][7] + dp[i - 1][9]
        dp[i][3] = dp[i - 1][4] + dp[i - 1][8]
        dp[i][4] = dp[i - 1][3] + dp[i - 1][9] + dp[i - 1][0]
        dp[i][6] = dp[i - 1][1] + dp[i - 1][7] + dp[i - 1][0]
        dp[i][7] = dp[i - 1][2] + dp[i - 1][6]
        dp[i][8] = dp[i - 1][1] + dp[i - 1][3]
        dp[i][9] = dp[i - 1][2] + dp[i - 1][4]

    total = sum(dp[N - 1]) 
    return total


with open('input17.txt', 'r') as file:
    N = int(file.readline())

result = count_phone_numbers(N)

with open('output17.txt', 'w') as file:
    file.write(str(result))
