# main.py

import task1_linked_list as t1
import task2_pythagoras_tree as t2
import task3_dijkstra as t3
import task4_heap_visualization as t4
import task5_tree_traversals as t5
import task6_greedy_dp as t6
import task7_monte_carlo_dice as t7

def run_task1():
    print("\n=== Завдання 1: Однозв'язний список ===")
    ll1 = t1.LinkedList()
    for val in [3, 1, 4]:
        ll1.append(val)
    print("Початковий список 1:", ll1.to_list())
    ll1.insertion_sort()
    print("Відсортований список 1:", ll1.to_list())

    ll2 = t1.LinkedList()
    for val in [2, 5, 0]:
        ll2.append(val)
    print("Початковий список 2:", ll2.to_list())
    ll2.insertion_sort()
    print("Відсортований список 2:", ll2.to_list())

    merged_head = t1.merge_sorted_lists(ll1.head, ll2.head)
    merged_list = t1.LinkedList()
    merged_list.head = merged_head
    print("Об’єднаний відсортований список:", merged_list.to_list())

def run_task2():
    print("\n=== Завдання 2: Дерево Піфагора (відкривається в окремому вікні) ===")
    level = int(input("Введіть рівень рекурсії для дерева Піфагора (наприклад, 5): "))
    t2.draw_pythagoras_tree(level)

def run_task3():
    print("\n=== Завдання 3: Алгоритм Дейкстри ===")
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    distances = t3.dijkstra(graph, 'A')
    print("Найкоротші відстані від A:", distances)

def run_task4():
    print("\n=== Завдання 4: Візуалізація бінарної купи (відкривається в окремому вікні) ===")
    heap = [10, 9, 8, 5, 6, 7, 4]
    root = t4.build_heap_tree(heap)
    t4.draw_tree(root)

def run_task5():
    print("\n=== Завдання 5: Обходи дерева DFS та BFS (відкривається в окремому вікні) ===")
    root = t5.create_sample_tree()
    print("Виконуємо DFS...")
    t5.visualize_dfs(root)
    print("Виконуємо BFS...")
    t5.visualize_bfs(root)

def run_task6():
    print("\n=== Завдання 6: Жадібний алгоритм і динамічне програмування ===")
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 100
    greedy_result = t6.greedy_algorithm(items, budget)
    dp_result = t6.dynamic_programming(items, budget)
    print(f"Жадібний алгоритм (бюджет {budget}):", greedy_result)
    print(f"Динамічне програмування (бюджет {budget}):", dp_result)

def run_task7():
    print("\n=== Завдання 7: Метод Монте-Карло для кидків кубиків ===")
    trials = 100000
    probabilities = t7.monte_carlo_dice_simulation(trials)
    print(f"Імовірності сум за {trials} симуляцій:")
    for s in sorted(probabilities):
        print(f"Сума {s}: {probabilities[s]:.4f}")
    t7.plot_probabilities(probabilities)

def main():
    run_task1()
    run_task2()
    run_task3()
    run_task4()
    run_task5()
    run_task6()
    run_task7()

if __name__ == "__main__":
    main()
