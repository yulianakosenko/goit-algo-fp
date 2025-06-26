# task6_greedy_dp.py

def greedy_algorithm(items, budget):
    # Сортуємо за калоріями на одиницю вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories']/x[1]['cost'], reverse=True)
    total_cost = 0
    chosen = []
    for name, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            chosen.append(name)
            total_cost += data['cost']
    return chosen

def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[n]['cost'] for n in names]
    calories = [items[n]['calories'] for n in names]
    n = len(items)

    dp = [[0]*(budget+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(budget+1):
            if costs[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - costs[i-1]] + calories[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    w = budget
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen.append(names[i-1])
            w -= costs[i-1]
    chosen.reverse()
    return chosen
