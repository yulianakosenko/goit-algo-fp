# task7_monte_carlo_dice.py

import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(trials=100000):
    counts = {i: 0 for i in range(2, 13)}
    for _ in range(trials):
        roll_sum = random.randint(1,6) + random.randint(1,6)
        counts[roll_sum] += 1
    probabilities = {k: v/trials for k,v in counts.items()}
    return probabilities

def plot_probabilities(probabilities):
    sums = sorted(probabilities.keys())
    probs = [probabilities[s] for s in sums]

    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність сум при киданні двох кубиків (метод Монте-Карло)')
    plt.xticks(sums)
    plt.show()
