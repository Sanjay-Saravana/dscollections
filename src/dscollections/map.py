"""Hash-based map/set wrappers with consistent DS-style API."""

from __future__ import annotations

from typing import Generic, Iterator, TypeVar

K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("T")


class HashMap(Generic[K, V]):
    def __init__(self) -> None:
        self._data: dict[K, V] = {}

    def put(self, key: K, value: V) -> None:
        self._data[key] = value

    def get(self, key: K) -> V:
        if key not in self._data:
            raise KeyError(key)
        return self._data[key]

    def remove(self, key: K) -> V:
        if key not in self._data:
            raise KeyError(key)
        return self._data.pop(key)

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[K]:
        return iter(self._data)

    def __repr__(self) -> str:
        return f"HashMap({self._data!r})"


class HashSet(Generic[T]):
    def __init__(self) -> None:
        self._data: set[T] = set()

    def add(self, value: T) -> None:
        self._data.add(value)

    def remove(self, value: T) -> None:
        self._data.remove(value)

    def contains(self, value: T) -> bool:
        return value in self._data

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)

    def __repr__(self) -> str:
        return f"HashSet({sorted(self._data)!r})"
