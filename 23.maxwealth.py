def maximumWealth(self, accounts: list[list[int]]) -> int:
    maxWealth = 0
    for i in range(len(accounts)):
        totalWealth = sum(accounts[i])
        maxWealth = max(maxWealth, totalWealth)
    return maxWealth
# Input list of customer wealth
accounts = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

# Calculate maximum wealth using the method
result = maximumWealth(None, accounts)
print(result)
