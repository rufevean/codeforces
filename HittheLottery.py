amount = int(input())
coins = [1,5,10,20,100]
dp = {}
def helper(curr,den):
    global coins
    if (curr,den) in dp:
        return dp[curr,den]
    if den == 0 or curr % coins[den] ==0:
        dp[curr,den] = curr //coins[den]
        return dp[curr,den]
    take = 1e9
    if coins[den] <= curr:
        cut = curr%coins[den]
        take = curr//coins[den]+helper(cut,den)
    not_take = helper(curr,den-1)
    dp[curr,den] = min(take,not_take)
    return min(take,not_take)

ans = helper(amount,4)
print(ans)
