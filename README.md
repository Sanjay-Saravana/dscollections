# dscollections

`dscollections` is a professional, production-quality Python package for **Data Structures and Algorithms (DSA)**.

Author: **Sanjay Saravanan**
Version: **0.2.0**

## Key Highlights

- Professional package layout (`src/` style) with PyPI-ready metadata.
- Rich collection of commonly used data structures.
- Type-hinted APIs for maintainable code and IDE support.
- Readable object representations: printing a DS shows its contents.
- Unit tested using `pytest`.

## Included Data Structures

### Linear
- `DynamicArray[T]`
- `Stack[T]`
- `Queue[T]`
- `Deque[T]`
- `CircularQueue[T]`
- `SinglyLinkedList[T]`
- `DoublyLinkedList[T]`

### Trees
- `BinarySearchTree[T]`

### Graphs
- `Graph[T]` (directed or undirected)

### Heaps & Priority
- `MinHeap[T]`
- `MaxHeap[T]`
- `PriorityQueue[T]`

### Hash Structures
- `HashMap[K, V]`
- `HashSet[T]`

### Advanced
- `Trie`
- `DisjointSet[T]` (Union-Find)

## Installation

```bash
pip install dscollections
```

Development mode:

```bash
pip install -e .[dev]
```

## Print-friendly Behavior

All data structures implement informative `__repr__`, so printing displays content directly.

```python
from dscollections import Stack, Queue, BinarySearchTree, HashMap

stack = Stack([1, 2, 3])
queue = Queue(["a", "b"]) 
bst = BinarySearchTree[int]()
for x in [10, 5, 15]:
    bst.insert(x)

m = HashMap[str, int]()
m.put("x", 100)

print(stack)  # Stack(top->bottom=[3, 2, 1])
print(queue)  # Queue(front->rear=['a', 'b'])
print(bst)    # BinarySearchTree(in_order=[5, 10, 15])
print(m)      # HashMap({'x': 100})
```

## Publishing to PyPI

1. Build package:
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

## License

MIT License
