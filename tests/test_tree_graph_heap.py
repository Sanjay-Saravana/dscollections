from dscollections import BinarySearchTree, Graph, MaxHeap, MinHeap, PriorityQueue


def test_bst_insertion_and_traversal() -> None:
    bst = BinarySearchTree[int]()
    for value in [10, 5, 15, 12, 18, 5]:
        bst.insert(value)
    assert list(bst.in_order()) == [5, 10, 12, 15, 18]
    assert list(bst.pre_order())[0] == 10
    assert "in_order" in repr(bst)


def test_graph_bfs_and_dfs() -> None:
    graph = Graph[str](directed=False)
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    assert set(graph.bfs("A")) == {"A", "B", "C", "D"}
    assert set(graph.dfs("A")) == {"A", "B", "C", "D"}
    assert "adjacency" in repr(graph)


def test_heaps_and_priority_queue() -> None:
    min_heap = MinHeap([5, 2, 7])
    min_heap.push(1)
    assert min_heap.pop() == 1

    max_heap = MaxHeap([5, 2, 7])
    max_heap.push(10)
    assert max_heap.pop() == 10

    pq = PriorityQueue[str]()
    pq.put("low", priority=5)
    pq.put("high", priority=1)
    assert pq.get() == "high"
