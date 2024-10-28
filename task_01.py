#Набір доступних монет
coins = [50, 25, 10, 5, 2, 1]

#Жадібний алгоритм для пошуку монет
def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            result[coin] = num_coins
            amount -= coin * num_coins
    return result

#Алгоритм динамічного програмування для пошуку мінімальної кількості монет
def find_min_coins(amount):
    
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 
    coin_used = [0] * (amount + 1)

   
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:  
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin == 0:  
            break  
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


amount = 113
print("Результат жадібного алгоритму:", find_coins_greedy(amount))
print("Результат алгоритму динамічного програмування:", find_min_coins(amount))
