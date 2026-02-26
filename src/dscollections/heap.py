"""Heap and priority queue data structures."""

from __future__ import annotations

import heapq
from typing import Generic, Iterable, TypeVar

T = TypeVar("T")


class MinHeap(Generic[T]):
    """Minimum heap."""

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._heap = list(values) if values is not None else []
        heapq.heapify(self._heap)

    def push(self, value: T) -> None:
        heapq.heappush(self._heap, value)

    def pop(self) -> T:
        if not self._heap:
            raise IndexError("pop from empty MinHeap")
        return heapq.heappop(self._heap)

    def peek(self) -> T:
        if not self._heap:
            raise IndexError("peek from empty MinHeap")
        return self._heap[0]

    def __len__(self) -> int:
        return len(self._heap)

    def __repr__(self) -> str:
        return f"MinHeap(sorted={sorted(self._heap)!r})"


class MaxHeap(Generic[T]):
    """Maximum heap for numeric/comparable values."""

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._heap: list[tuple[T, T]] = []
        if values is not None:
            for value in values:
                self.push(value)

    def push(self, value: T) -> None:
        heapq.heappush(self._heap, (-value, value))  # type: ignore[operator]

    def pop(self) -> T:
        if not self._heap:
            raise IndexError("pop from empty MaxHeap")
        return heapq.heappop(self._heap)[1]

    def peek(self) -> T:
        if not self._heap:
            raise IndexError("peek from empty MaxHeap")
        return self._heap[0][1]

    def __len__(self) -> int:
        return len(self._heap)

    def __repr__(self) -> str:
        return f"MaxHeap(sorted_desc={sorted((item[1] for item in self._heap), reverse=True)!r})"


class PriorityQueue(Generic[T]):
    """Min-priority queue where lower integer priority is dequeued first."""

    def __init__(self) -> None:
        self._heap: list[tuple[int, int, T]] = []
        self._seq = 0

    def put(self, item: T, priority: int = 0) -> None:
        self._seq += 1
        heapq.heappush(self._heap, (priority, self._seq, item))

    def get(self) -> T:
        if not self._heap:
            raise IndexError("get from empty PriorityQueue")
        return heapq.heappop(self._heap)[2]

    def __len__(self) -> int:
        return len(self._heap)

    def __repr__(self) -> str:
        view = [(p, item) for p, _, item in sorted(self._heap)]
        return f"PriorityQueue(items={view!r})"
