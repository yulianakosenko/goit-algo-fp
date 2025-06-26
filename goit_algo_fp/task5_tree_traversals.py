# task5_tree_traversals.py

import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def create_sample_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, label=node.val, color=node.color)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def visualize_tree(root, visited_nodes):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    # Визначаємо кольори залежно від порядку обходу
    color_map = {}
    base_color = (18, 150, 240)  # RGB #1296F0
    max_visits = len(visited_nodes)
    for i, node_id in enumerate(visited_nodes):
        # Колір змінюємо від темного до світлого, лінійно
        factor = i / max_visits
        r = int(base_color[0] + (255 - base_color[0]) * factor)
        g = int(base_color[1] + (255 - base_color[1]) * factor)
        b = int(base_color[2] + (255 - base_color[2]) * factor)
        color_map[node_id] = f"#{r:02X}{g:02X}{b:02X}"

    colors = []
    for node in tree.nodes():
        colors.append(color_map.get(node, "#D3D3D3"))  # сірий для не відвіданих

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def visualize_dfs(root):
    stack = [root]
    visited_order = []
    visited_set = set()
    while stack:
        node = stack.pop()
        if node.id not in visited_set:
            visited_order.append(node.id)
            visited_set.add(node.id)
            # Додаємо праву дитину, щоб ліва оброблялась першою
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    visualize_tree(root, visited_order)

def visualize_bfs(root):
    queue = deque([root])
    visited_order = []
    visited_set = set()
    while queue:
        node = queue.popleft()
        if node.id not in visited_set:
            visited_order.append(node.id)
            visited_set.add(node.id)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    visualize_tree(root, visited_order)
