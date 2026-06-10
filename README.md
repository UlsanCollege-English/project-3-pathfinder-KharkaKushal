[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/RNukvtFO)
# Project 3: Pathfinder

> Student note: You must complete this README. Do not leave the TODO text in your final submission.

## Map Theme

A summer music festival map. The graph models locations at an outdoor festival where attendees walk between stages, food areas, and services.

## Map Picture

![Project map](assets/map.png)

*Map image placeholder - please add your drawn map as `assets/map.png`*

## How the Graph Works

### Nodes

Each node is a location at the music festival.

```text
- Gate: Main entrance/exit
- Food Court: Food vendors and seating area
- Main Stage: Primary concert stage
- Rest Area: Seating and shade for resting
- First Aid: Medical services station
- Game Booth: Carnival games and prizes
```

### Edges

Each edge is a walking path connecting two festival locations. The graph is undirected, so paths can be traveled in both directions.

```text
- Gate ↔ Food Court
- Gate ↔ Main Stage
- Food Court ↔ Rest Area
- Main Stage ↔ First Aid
- Rest Area ↔ Game Booth
- First Aid ↔ Game Booth
```

### Weights

Each weight is the walking time in minutes between two connected locations.

```text
- Gate → Food Court: 4 minutes
- Gate → Main Stage: 7 minutes
- Food Court → Rest Area: 3 minutes
- Main Stage → First Aid: 2 minutes
- Rest Area → Game Booth: 5 minutes
- First Aid → Game Booth: 6 minutes
```

## Features Implemented

Check the features you completed:

- [x] Load graph from JSON
- [x] Get neighbors
- [x] BFS traversal
- [x] Dijkstra shortest distances
- [x] Shortest path reconstruction
- [x] Demo function
- [x] Extra tests
- [ ] Stretch feature: TODO

## How to Run

```bash
python src/project.py
```

This runs the `demo()` function which prints:
1. The graph loaded from `data/map.json`
2. Number of locations (6 nodes, 12 edges)
3. BFS order from "Gate"
4. Shortest distances from "Gate"
5. Shortest path from "Gate" to "Game Booth"

## How to Test

```bash
pytest -q
```

## Complexity

### BFS

Time:
```text
O(V + E)
```

Space:
```text
O(V)
```

Explanation:
- V = number of vertices (locations)
- E = number of edges (paths)
- BFS visits each node at most once and checks each connection. The queue holds at most V nodes.

### Dijkstra

Time:
```text
O((V + E) log V)
```

Space:
```text
O(V)
```

Explanation:
- Dijkstra tracks shortest known distances to each node.
- The `heapq` priority queue operations (push/pop) add the `log V` factor.
- Each node is processed once, each edge is relaxed once.

### Shortest Path Reconstruction

Time:
```text
O(P)
```

Space:
```text
O(P)
```

Explanation:
- P = number of nodes in the returned path.
- Rebuilding the path follows the previous-node chain from target back to start, then reverses.

## Edge Cases

Check the edge cases your project handles:

- [x] Empty graph (handled by missing start returning empty)
- [x] Missing start node (returns `[]` or `{}`)
- [x] Missing target node (returns `[]`)
- [x] Start equals target (returns `[start]`)
- [x] Unreachable target (returns `[]` - disconnected components)
- [x] Graph with a cycle (BFS visited set prevents infinite loops)
- [x] Graph with one node (works correctly)
- [x] Disconnected graph (unreachable nodes not included in Dijkstra)
- [x] Multiple possible paths (Dijkstra finds shortest)
- [x] Zero weight rejected (raises `ValueError`)
- [x] Negative weight rejected (raises `ValueError`)

Add notes about edge cases here:

The implementation validates all weights on load and during Dijkstra/shortest_path to ensure positive integers only. Missing nodes return empty results rather than raising errors, following the specification. BFS uses a visited set to handle cycles correctly.

## Known Limitations

- Does not support directed graphs (all edges are bidirectional).
- Does not support negative weights (raises `ValueError`).
- Does not use a GUI (console output only).
- Tie paths may return one valid shortest path, not all shortest paths.
- Map image is a placeholder; needs a hand-drawn map added as `assets/map.png`.

## Assistance & Sources

### AI Used?

Yes

### What AI Helped With

- Explaining Dijkstra algorithm implementation details
- Debugging test failures for edge cases
- Suggesting additional edge case tests
- Improving README wording and formatting

### Other Sources

- Course materials on graph algorithms (BFS, Dijkstra)
- Python `heapq` documentation for priority queue
- Python `collections.deque` documentation for BFS queue
- Project 3 brief and starter code from classroom repository