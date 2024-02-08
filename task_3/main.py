import heapq


def dijkstra_heap(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        print(heap)

        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


if __name__ == '__main__':
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 10, 'C': 4},
        'C': {'A': 10, 'B': 4, 'D': 2},
        'D': {'B': 10, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }

    start_vertex = 'A'
    shortest_distances = dijkstra_heap(graph, start_vertex)
    print("Найкоротші відстані від вершини", start_vertex + ":")

    for vertex, distance in shortest_distances.items():
        print(f"Від {start_vertex} до {vertex}: {distance}")

