"""Additional high-value DSA structures."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Generic, TypeVar

T = TypeVar("T")


class DisjointSet(Generic[T]):
    """Union-Find / Disjoint Set Union (DSU)."""

    def __init__(self) -> None:
        self._parent: Dict[T, T] = {}
        self._rank: Dict[T, int] = {}

    def make_set(self, item: T) -> None:
        if item not in self._parent:
            self._parent[item] = item
            self._rank[item] = 0

    def find(self, item: T) -> T:
        if item not in self._parent:
            self.make_set(item)
        parent = self._parent[item]
        if parent != item:
            self._parent[item] = self.find(parent)
        return self._parent[item]

    def union(self, a: T, b: T) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self._rank[ra] < self._rank[rb]:
            self._parent[ra] = rb
        elif self._rank[ra] > self._rank[rb]:
            self._parent[rb] = ra
        else:
            self._parent[rb] = ra
            self._rank[ra] += 1

    def connected(self, a: T, b: T) -> bool:
        return self.find(a) == self.find(b)

    def __repr__(self) -> str:
        groups: Dict[T, list[T]] = {}
        for item in self._parent:
            groups.setdefault(self.find(item), []).append(item)
        normalized = {root: sorted(items) for root, items in groups.items()}
        return f"DisjointSet(groups={normalized!r})"


@dataclass
class _TrieNode:
    children: dict[str, _TrieNode] = field(default_factory=dict)
    is_end: bool = False


class Trie:
    """Prefix tree for string keys."""

    def __init__(self) -> None:
        self._root = _TrieNode()
        self._size = 0

    def insert(self, word: str) -> None:
        node = self._root
        for ch in word:
            node = node.children.setdefault(ch, _TrieNode())
        if not node.is_end:
            node.is_end = True
            self._size += 1

    def search(self, word: str) -> bool:
        node = self._root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self._root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"Trie(size={self._size})"
