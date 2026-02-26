"""Tree data structures with printable content views."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generator, Generic, TypeVar

T = TypeVar("T")


@dataclass
class _BSTNode(Generic[T]):
    value: T
    left: _BSTNode[T] | None = None
    right: _BSTNode[T] | None = None


class BinarySearchTree(Generic[T]):
    """Unbalanced binary search tree."""

    def __init__(self) -> None:
        self._root: _BSTNode[T] | None = None
        self._size = 0

    def insert(self, value: T) -> None:
        if self._root is None:
            self._root = _BSTNode(value)
            self._size += 1
            return
        current = self._root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = _BSTNode(value)
                    self._size += 1
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = _BSTNode(value)
                    self._size += 1
                    return
                current = current.right
            else:
                return

    def contains(self, value: T) -> bool:
        cur = self._root
        while cur is not None:
            if value < cur.value:
                cur = cur.left
            elif value > cur.value:
                cur = cur.right
            else:
                return True
        return False

    def in_order(self) -> Generator[T, None, None]:
        def walk(node: _BSTNode[T] | None) -> Generator[T, None, None]:
            if node is None:
                return
            yield from walk(node.left)
            yield node.value
            yield from walk(node.right)

        yield from walk(self._root)

    def pre_order(self) -> Generator[T, None, None]:
        def walk(node: _BSTNode[T] | None) -> Generator[T, None, None]:
            if node is None:
                return
            yield node.value
            yield from walk(node.left)
            yield from walk(node.right)

        yield from walk(self._root)

    def post_order(self) -> Generator[T, None, None]:
        def walk(node: _BSTNode[T] | None) -> Generator[T, None, None]:
            if node is None:
                return
            yield from walk(node.left)
            yield from walk(node.right)
            yield node.value

        yield from walk(self._root)

    def __contains__(self, value: T) -> bool:
        return self.contains(value)

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"BinarySearchTree(in_order={list(self.in_order())!r})"
