# dscollections

`dscollections` is a professional, educational, and production-friendly Python package that provides commonly used **Data Structures and Algorithms (DSA)** building blocks.

Author: **Sanjay Saravanan M.Tech (IIT MADRAS)**

## Why dscollections?

- Clean and consistent APIs.
- Strong type hints for better IDE support.
- Thorough inline documentation.
- Easy to install and publish on PyPI.
- Tested with `pytest`.

## Included Data Structures

### Linear
- `DynamicArray[T]`
- `Stack[T]`
- `Queue[T]`
- `Deque[T]`
- `SinglyLinkedList[T]`

### Trees
- `BinarySearchTree[T]`

### Graphs
- `Graph[T]` (adjacency-list based)

### Priority Structures
- `MinHeap[T]`

## Installation

```bash
pip install dscollections
```

For local development:

```bash
pip install -e .[dev]
```

## Quick Start

```python
from dscollections import Stack, Queue, BinarySearchTree

stack = Stack[int]()
stack.push(10)
stack.push(20)
print(stack.pop())   # 20

queue = Queue[str]()
queue.enqueue("a")
queue.enqueue("b")
print(queue.dequeue())  # "a"

bst = BinarySearchTree[int]()
for value in [10, 5, 15, 12]:
    bst.insert(value)

print(12 in bst)          # True
print(list(bst.in_order()))  # [5, 10, 12, 15]
```

## Publishing to PyPI

1. Build distributions:
   ```bash
   python -m pip install --upgrade build
   python -m build
   ```
2. Upload to TestPyPI:
   ```bash
   python -m pip install --upgrade twine
   twine upload --repository testpypi dist/*
   ```
3. Upload to PyPI:
   ```bash
   twine upload dist/*
   ```

## Project Layout

```text
src/dscollections/
  __init__.py
  linear.py
  tree.py
  graph.py
  heap.py
tests/
```

## License

MIT License
