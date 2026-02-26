"""dscollections: Professional data structures package for Python."""

from .advanced import DisjointSet, Trie
from .graph import Graph
from .heap import MaxHeap, MinHeap, PriorityQueue
from .linear import (
    CircularQueue,
    Deque,
    DoublyLinkedList,
    DynamicArray,
    Queue,
    SinglyLinkedList,
    Stack,
)
from .map import HashMap, HashSet
from .tree import BinarySearchTree

__all__ = [
    "DynamicArray",
    "Stack",
    "Queue",
    "Deque",
    "CircularQueue",
    "SinglyLinkedList",
    "DoublyLinkedList",
    "BinarySearchTree",
    "Graph",
    "MinHeap",
    "MaxHeap",
    "PriorityQueue",
    "HashMap",
    "HashSet",
    "DisjointSet",
    "Trie",
]
