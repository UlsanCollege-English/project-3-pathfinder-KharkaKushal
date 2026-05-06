# Project 3: Pathfinder

## Due

**Wednesday, 2026-05-26, 23:59 KST**

## Project Type

This is an **individual project**.

You may discuss ideas and debugging strategies with classmates, but the code, tests, README, and map must be your own work.

## Goal

Build a small pathfinding tool using a weighted graph.

Your program will model a map as connected locations, then use graph algorithms to explore the map and find shortest paths.

Your map may be realistic or fictional.

Examples:

- Ulsan College campus
- subway or bus stops
- museum rooms
- festival booths
- delivery locations
- airport terminal
- game dungeon
- fantasy village
- theme park attractions

The important rule:

> Your project must actually be a graph.

That means it must have locations connected by paths. It should not just be a list of places.

---

## Required Concept

Your graph must be an **undirected weighted graph**.

- **Undirected** means paths go both ways.
- **Weighted** means each path has a cost.
- Costs must be **positive integers**.
- No zero weights.
- No negative weights.

Weights may represent:

- walking time
- distance
- travel cost
- danger level
- energy required
- crowd difficulty
- difficulty level

Example:

```text
Gate --4-- Food Court
Gate --7-- Main Stage
Food Court --3-- Rest Area
```

---

## Recommended Map Size

Recommended:

- **8–12 nodes**
- **10–16 edges**

You may make a larger map if you want a challenge, but do not make the project too large to test carefully.

A smaller correct project is better than a giant broken one.

---

## Required Visual Map

You must draw your map and include a picture of it in your repo.

Required:

```text
assets/map.png
```

Allowed alternatives:

```text
assets/map.jpg
assets/map.jpeg
```

Your README must show the image:

```md
![Project map](assets/map.png)
```

Your drawing does not need to be beautiful. It must be clear.

It should show:

- all locations/nodes,
- all paths/edges,
- the weight for each edge.

---

## Required Repo Structure

Your repo should contain:

```text
src/
  project.py

tests/
  test_project.py

data/
  map.json

assets/
  map.png

README.md
```

You may add helper files only if they make your project clearer.

Do not submit notebooks as graded work.

---

## Required JSON Format

Your map data must be stored in:

```text
data/map.json
```

Use this format:

```json
{
  "Gate": {
    "Food Court": 4,
    "Main Stage": 7
  },
  "Food Court": {
    "Gate": 4,
    "Rest Area": 3
  },
  "Main Stage": {
    "Gate": 7,
    "First Aid": 2
  }
}
```

This is called a **dictionary of dictionaries**.

In Python, the graph type is:

```python
Graph = dict[str, dict[str, int]]
```

Because this project uses an undirected graph, every edge should appear in both directions.

Example:

```json
{
  "A": {
    "B": 5
  },
  "B": {
    "A": 5
  }
}
```

---

## Required Functions

Implement these functions in `src/project.py`.

### `load_graph`

```python
def load_graph(path: str) -> Graph:
    """Load a weighted graph from a JSON file."""
```

Requirements:

- Load the JSON file.
- Return the graph.
- Raise `ValueError` if the graph format is invalid.
- Raise `ValueError` if any weight is zero or negative.
- Raise `ValueError` if any weight is not an integer.

---

### `get_neighbors`

```python
def get_neighbors(graph: Graph, node: str) -> dict[str, int]:
    """Return neighbors and weights for node."""
```

Requirements:

- If the node exists, return its neighbors.
- If the node is missing, return `{}`.

---

### `bfs_order`

```python
def bfs_order(graph: Graph, start: str) -> list[str]:
    """Return nodes in breadth-first traversal order."""
```

Requirements:

- Use a queue.
- Use a visited set.
- If `start` is missing, return `[]`.
- Follow the neighbor order from the dictionary.
- Ignore weights for BFS traversal.

---

### `dijkstra_distances`

```python
def dijkstra_distances(graph: Graph, start: str) -> dict[str, float]:
    """Return shortest distances from start to every reachable node."""
```

Requirements:

- Use Dijkstra’s algorithm.
- Use `heapq` as the priority queue.
- If `start` is missing, return `{}`.
- Return distances only for reachable nodes.
- Raise `ValueError` if a zero or negative weight is found.

---

### `shortest_path`

```python
def shortest_path(graph: Graph, start: str, target: str) -> list[str]:
    """Return the shortest path from start to target."""
```

Requirements:

- Use Dijkstra’s algorithm with path reconstruction.
- Return a list of node names.
- If `start` or `target` is missing, return `[]`.
- If `target` is unreachable, return `[]`.
- If `start == target`, return `[start]`.

---

### `demo`

```python
def demo() -> None:
    """Print a short demonstration of your project."""
```

Your demo should show:

1. the graph loading from `data/map.json`,
2. the number of locations,
3. BFS order from one location,
4. shortest distances from one location,
5. one shortest path from one location to another.

---

## Required Tests

The starter tests are not enough.

You must add at least **3 meaningful tests** of your own.

Good test ideas:

- your own map loads correctly,
- missing start node,
- missing target node,
- unreachable target,
- graph with a cycle,
- graph with one node,
- shortest path with multiple possible routes,
- zero weight raises `ValueError`,
- negative weight raises `ValueError`.

Run tests with:

```bash
pytest -q
```

---

## Required README

You must complete `README.md`.

Your README must explain:

- your map theme,
- what the nodes represent,
- what the edges represent,
- what the weights represent,
- how to run the project,
- how to test the project,
- BFS complexity,
- Dijkstra complexity,
- path reconstruction complexity,
- edge cases,
- assistance and sources.

---

## Complexity Expectations

Include these in your README.

### BFS

Expected:

```text
Time: O(V + E)
Space: O(V)
```

Explain:

- `V` = number of vertices/nodes
- `E` = number of edges/connections
- BFS visits each node at most once and checks connections.

### Dijkstra

Expected:

```text
Time: O((V + E) log V)
Space: O(V)
```

Explain:

- Dijkstra tracks shortest known distances.
- `heapq` priority queue operations add the `log V` factor.

### Path Reconstruction

Expected:

```text
Time: O(P)
Space: O(P)
```

Explain:

- `P` = number of nodes in the returned path.
- Rebuilding the path follows the previous-node chain from target back to start.

---

## Standards Targeted

### Primary

**S12 — Graphs + BFS/DFS + Dijkstra**

You show evidence by using:

- adjacency list graph representation,
- BFS traversal,
- Dijkstra shortest distances,
- path reconstruction,
- unreachable-node handling.

### Supporting

- **S3 — Big-O reasoning**
- **S6 — dict/set**
- **S7 — queue**
- **S11 — heapq / priority queue**

---

## Grading Rubric

| Category | Points |
|---|---:|
| Functionality & correctness | 30 |
| Data structure / algorithm appropriateness + justification | 20 |
| Code quality & architecture | 15 |
| Testing depth | 15 |
| Documentation & demo | 10 |
| Presentation / Q&A | 10 |
| **Total** | **100** |

---

## Meets / Exceeds / Not Yet Guidance

### Meets

Your project is at Meets level if:

- required functions work,
- starter tests pass,
- your own map loads from JSON,
- BFS works,
- Dijkstra distances are correct,
- shortest path works for normal cases,
- README explains graph structure and complexity,
- code is readable.

### Exceeds

Your project may reach Exceeds level if:

- tests include strong edge cases,
- path reconstruction handles tricky cases cleanly,
- code is clean and well-organized,
- README explains tradeoffs clearly,
- demo is polished,
- you add a useful stretch feature without breaking the core requirements.

Good stretch features:

- DFS traversal,
- route summary with total cost,
- blocked-location feature,
- directed graph support,
- predictable tie-case handling,
- simple command-line menu.

### Not Yet

Your project is Not Yet if:

- required functions are missing,
- code does not run,
- tests fail,
- Dijkstra is incorrect,
- shortest path is hardcoded,
- map is not really a graph,
- README is incomplete,
- map picture is missing,
- zero or negative weights are allowed.

---

## Final Submission Checklist

Before the deadline, check:

- [ ] `src/project.py` has all required functions implemented.
- [ ] `tests/test_project.py` passes.
- [ ] I added at least 3 meaningful tests of my own.
- [ ] `data/map.json` contains my project map.
- [ ] `assets/map.png` or another allowed image file shows my drawn map.
- [ ] README embeds the map picture.
- [ ] README explains nodes, edges, and weights.
- [ ] README includes complexity explanations.
- [ ] README includes edge cases.
- [ ] README includes assistance and sources.
- [ ] `pytest -q` passes locally.
