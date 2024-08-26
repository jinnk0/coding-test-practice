N, K = map(int, input().split())

coins = []

for i in range(N):
    coins.append(int(input()))
  
count = 0

while (K > 0):
    coin = coins.pop()
    if coin <= K:
        count += K // coin
        K %= coin
        
print(count)
        