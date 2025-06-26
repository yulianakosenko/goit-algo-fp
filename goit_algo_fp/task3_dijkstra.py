# task3_dijkstra.py

import heapq

def dijkstra(graph, start):
    heap = []
    heapq.heappush(heap, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    while heap:
        curr_dist, curr_node = heapq.heappop(heap)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances
