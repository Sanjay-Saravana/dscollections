"""Linear data structures.

This module provides a range of list-like data structures commonly used in DSA,
all with readable string representations that show their current contents.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque as TypingDeque
from typing import Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")


class DynamicArray(Generic[T]):
    """A resizable contiguous array abstraction."""

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._data: list[T] = list(values) if values is not None else []

    def append(self, value: T) -> None:
        self._data.append(value)

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty DynamicArray")
        return self._data.pop()

    def insert(self, index: int, value: T) -> None:
        self._data.insert(index, value)

    def remove(self, value: T) -> None:
        self._data.remove(value)

    def get(self, index: int) -> T:
        return self._data[index]

    def set(self, index: int, value: T) -> None:
        self._data[index] = value

    def to_list(self) -> list[T]:
        return list(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)

    def __repr__(self) -> str:
        return f"DynamicArray({self._data!r})"


class Stack(Generic[T]):
    """LIFO stack."""

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._items: list[T] = list(values) if values is not None else []

    def push(self, value: T) -> None:
        self._items.append(value)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty Stack")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from empty Stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack(top->bottom={list(reversed(self._items))!r})"


class Queue(Generic[T]):
    """FIFO queue."""

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._items: TypingDeque[T] = deque(values or [])

    def enqueue(self, value: T) -> None:
        self._items.append(value)

    def dequeue(self) -> T:
        if not self._items:
            raise IndexError("dequeue from empty Queue")
        return self._items.popleft()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from empty Queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Queue(front->rear={list(self._items)!r})"


class Deque(Generic[T]):
    """Double-ended queue."""

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._items: TypingDeque[T] = deque(values or [])

    def append_left(self, value: T) -> None:
        self._items.appendleft(value)

    def append_right(self, value: T) -> None:
        self._items.append(value)

    def pop_left(self) -> T:
        if not self._items:
            raise IndexError("pop_left from empty Deque")
        return self._items.popleft()

    def pop_right(self) -> T:
        if not self._items:
            raise IndexError("pop_right from empty Deque")
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Deque(left->right={list(self._items)!r})"


class CircularQueue(Generic[T]):
    """Fixed-capacity circular queue."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self._capacity = capacity
        self._data: list[T | None] = [None] * capacity
        self._front = 0
        self._size = 0

    def enqueue(self, value: T) -> None:
        if self._size == self._capacity:
            raise OverflowError("enqueue to full CircularQueue")
        idx = (self._front + self._size) % self._capacity
        self._data[idx] = value
        self._size += 1

    def dequeue(self) -> T:
        if self._size == 0:
            raise IndexError("dequeue from empty CircularQueue")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return value  # type: ignore[return-value]

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        items = [self._data[(self._front + i) % self._capacity] for i in range(self._size)]
        return f"CircularQueue(capacity={self._capacity}, front->rear={items!r})"


@dataclass
class _SNode(Generic[T]):
    value: T
    next: _SNode[T] | None = None


class SinglyLinkedList(Generic[T]):
    """Singly linked list."""

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._head: _SNode[T] | None = None
        self._tail: _SNode[T] | None = None
        self._size = 0
        if values:
            for value in values:
                self.append(value)

    def prepend(self, value: T) -> None:
        node = _SNode(value=value, next=self._head)
        self._head = node
        if self._tail is None:
            self._tail = node
        self._size += 1

    def append(self, value: T) -> None:
        node = _SNode(value=value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def pop_front(self) -> T:
        if self._head is None:
            raise IndexError("pop_front from empty SinglyLinkedList")
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.value

    def __iter__(self) -> Iterator[T]:
        cur = self._head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList({list(self)!r})"


@dataclass
class _DNode(Generic[T]):
    value: T
    prev: _DNode[T] | None = None
    next: _DNode[T] | None = None


class DoublyLinkedList(Generic[T]):
    """Doubly linked list with front/back operations."""

    def __init__(self, values: Iterable[T] | None = None) -> None:
        self._head: _DNode[T] | None = None
        self._tail: _DNode[T] | None = None
        self._size = 0
        if values:
            for v in values:
                self.append(v)

    def append(self, value: T) -> None:
        node = _DNode(value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._size += 1

    def prepend(self, value: T) -> None:
        node = _DNode(value)
        if self._head is None:
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1

    def pop_front(self) -> T:
        if self._head is None:
            raise IndexError("pop_front from empty DoublyLinkedList")
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        else:
            self._head.prev = None
        self._size -= 1
        return node.value

    def pop_back(self) -> T:
        if self._tail is None:
            raise IndexError("pop_back from empty DoublyLinkedList")
        node = self._tail
        self._tail = node.prev
        if self._tail is None:
            self._head = None
        else:
            self._tail.next = None
        self._size -= 1
        return node.value

    def __iter__(self) -> Iterator[T]:
        cur = self._head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"DoublyLinkedList({list(self)!r})"
