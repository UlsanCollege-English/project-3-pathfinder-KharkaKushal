"""Project 3: Pathfinder.

Implement graph utilities for an undirected weighted map.

Rules:
- Python 3.11+
- stdlib only
- weights must be positive integers (no zero or negative weights)
- graph representation: dict[str, dict[str, int]]

Example graph:

    {
        "Gate": {
            "Food Court": 4,
            "Stage": 7,
        },
        "Food Court": {
            "Gate": 4,
            "Rest Area": 3,
        },
    }

Students:
- Replace each NotImplementedError with your implementation.
- Keep function names and parameters exactly as written.
- Add helper functions if they make your code clearer.
"""

from __future__ import annotations

from collections import deque
import heapq
import json
import math
from pathlib import Path


Graph = dict[str, dict[str, int]]


def load_graph(path: str) -> Graph:
    """Load a weighted graph from a JSON file.

    The JSON file must contain a dictionary of dictionaries:

        {
            "A": {"B": 3, "C": 5},
            "B": {"A": 3},
            "C": {"A": 5}
        }

    Requirements:
    - Return the loaded graph.
    - Raise ValueError if the JSON top level is not a dictionary.
    - Raise ValueError if any neighbor list is not a dictionary.
    - Raise ValueError if any weight is not a positive integer.
    - Raise ValueError if any weight is 0 or negative.

    Note:
    This project uses an undirected graph. Your own map should include both
    directions for every edge, such as A -> B and B -> A.
    """
    raise NotImplementedError


def get_neighbors(graph: Graph, node: str) -> dict[str, int]:
    """Return the neighbors and weights for node.

    If node is missing, return an empty dictionary.

    Example:
        graph = {"A": {"B": 4}}
        get_neighbors(graph, "A") -> {"B": 4}
        get_neighbors(graph, "Z") -> {}
    """
    raise NotImplementedError


def bfs_order(graph: Graph, start: str) -> list[str]:
    """Return nodes in breadth-first traversal order.

    Requirements:
    - If start is missing, return [].
    - Use a queue.
    - Use a visited set.
    - Follow the neighbor order from the dictionary.
    - Ignore weights for BFS traversal.

    Complexity target:
    - Time: O(V + E)
    - Space: O(V)
    """
    raise NotImplementedError


def dijkstra_distances(graph: Graph, start: str) -> dict[str, float]:
    """Return shortest distances from start to every reachable node.

    Requirements:
    - Use Dijkstra's algorithm.
    - Use heapq as the priority queue.
    - If start is missing, return {}.
    - Ignore unreachable nodes; they should not appear in the result.
    - All edge weights must be positive integers.
    - Raise ValueError if a zero or negative weight is found.

    Example:
        graph = {
            "A": {"B": 4, "C": 2},
            "B": {"A": 4},
            "C": {"A": 2}
        }

        dijkstra_distances(graph, "A") -> {"A": 0, "B": 4, "C": 2}

    Complexity target:
    - Time: O((V + E) log V)
    - Space: O(V)
    """
    raise NotImplementedError


def shortest_path(graph: Graph, start: str, target: str) -> list[str]:
    """Return the shortest path from start to target.

    Requirements:
    - Use Dijkstra's algorithm with path reconstruction.
    - Return a list of node names in path order.
    - If start or target is missing, return [].
    - If target is unreachable from start, return [].
    - If start == target and start exists, return [start].
    - Raise ValueError if a zero or negative weight is found.

    Example:
        shortest_path(graph, "A", "D") -> ["A", "C", "D"]

    Complexity target:
    - Dijkstra portion: O((V + E) log V)
    - Path reconstruction: O(P), where P is the number of nodes in the path
    """
    raise NotImplementedError


def demo() -> None:
    """Print a short demonstration of your project.

    Your demo should:
    1. Load your graph from data/map.json.
    2. Print the number of locations.
    3. Print BFS order from one location.
    4. Print shortest distances from one location.
    5. Print one shortest path.

    This function is not directly graded by the public tests, but it is useful
    for your presentation/demo.
    """
    raise NotImplementedError


if __name__ == "__main__":
    demo()
