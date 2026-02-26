"""Graph data structures."""

from __future__ import annotations

from collections import deque
from typing import Deque, Dict, Generic, Iterator, Set, TypeVar

T = TypeVar("T")


class Graph(Generic[T]):
    """Adjacency-list graph (directed by default)."""

    def __init__(self, directed: bool = True) -> None:
        self._adjacency: Dict[T, Set[T]] = {}
        self._directed = directed

    def add_vertex(self, vertex: T) -> None:
        self._adjacency.setdefault(vertex, set())

    def add_edge(self, source: T, destination: T) -> None:
        self.add_vertex(source)
        self.add_vertex(destination)
        self._adjacency[source].add(destination)
        if not self._directed:
            self._adjacency[destination].add(source)

    def neighbors(self, vertex: T) -> Set[T]:
        if vertex not in self._adjacency:
            raise KeyError(f"vertex {vertex!r} does not exist")
        return set(self._adjacency[vertex])

    def bfs(self, start: T) -> Iterator[T]:
        if start not in self._adjacency:
            raise KeyError(f"start vertex {start!r} does not exist")
        visited: Set[T] = {start}
        queue: Deque[T] = deque([start])
        while queue:
            node = queue.popleft()
            yield node
            for n in self._adjacency[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)

    def dfs(self, start: T) -> Iterator[T]:
        if start not in self._adjacency:
            raise KeyError(f"start vertex {start!r} does not exist")
        visited: Set[T] = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            yield node
            stack.extend(sorted(self._adjacency[node], reverse=True))

    def __len__(self) -> int:
        return len(self._adjacency)

    def __repr__(self) -> str:
        body = {k: sorted(v) for k, v in self._adjacency.items()}
        return f"Graph(directed={self._directed}, adjacency={body!r})"
