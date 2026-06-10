import heapq
import json
from collections import deque
from typing import TypeAlias, cast

Graph: TypeAlias = dict[str, dict[str, int]]


def load_graph(file_path: str) -> Graph:
    """Load a weighted graph from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        graph = json.load(file)

    for node in graph:
        for neighbor, weight in graph[node].items():
            if not isinstance(weight, int):
                raise ValueError("Graph weights must be integers")
            if weight <= 0:
                raise ValueError("Graph weights must be positive")

    return cast(Graph, graph)


def get_neighbors(graph: Graph, node: str) -> dict[str, int]:
    """Return neighbors and weights for node."""
    return graph.get(node, {})


def bfs_order(graph: Graph, start: str) -> list[str]:
    """Return nodes in breadth-first traversal order."""
    if start not in graph:
        return []

    visited = set()
    order = []
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dijkstra_distances(graph: Graph, start: str) -> dict[str, float]:
    """Return shortest distances from start to every reachable node."""
    if start not in graph:
        return {}

    for node in graph:
        for neighbor, weight in graph[node].items():
            if not isinstance(weight, int) or weight <= 0:
                raise ValueError("Graph weights must be positive integers")

    distances: dict[str, float] = {start: 0}
    priority_queue = [(0.0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


def shortest_path(graph: Graph, start: str, target: str) -> list[str]:
    """Return the shortest path from start to target."""
    if start not in graph or target not in graph:
        return []

    if start == target:
        return [start]

    for node in graph:
        for neighbor, weight in graph[node].items():
            if not isinstance(weight, int) or weight <= 0:
                raise ValueError("Graph weights must be positive integers")

    distances = {start: 0}
    previous = {}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == target:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    if target not in distances:
        return []

    path = []
    current = target

    while current != start:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    return path


def demo() -> None:
    """Print a short demonstration of the project."""
    graph = load_graph("data/map.json")

    print("=== Pathfinder Demo ===\n")

    print("Graph loaded from data/map.json")
    print(f"Number of locations: {len(graph)}")
    total_connections = sum(len(v) for v in graph.values()) // 2
    print(f"Number of connections: {total_connections}\n")

    print("--- BFS from 'Gate' ---")
    bfs_result = bfs_order(graph, "Gate")
    print(f"Order: {' -> '.join(bfs_result)}\n")

    print("--- Dijkstra distances from 'Gate' ---")
    distances = dijkstra_distances(graph, "Gate")
    for node, dist in sorted(distances.items()):
        print(f"  {node}: {dist} minutes")
    print()

    print("--- Shortest path: Gate to Game Booth ---")
    path = shortest_path(graph, "Gate", "Game Booth")
    if path:
        total_dist = distances["Game Booth"]
        print(f"Path: {' -> '.join(path)}")
        print(f"Total time: {total_dist} minutes")
    else:
        print("No path found")
