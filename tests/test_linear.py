from dscollections import (
    CircularQueue,
    Deque,
    DoublyLinkedList,
    DynamicArray,
    Queue,
    SinglyLinkedList,
    Stack,
)


def test_dynamic_array() -> None:
    arr = DynamicArray([1, 2])
    arr.append(3)
    arr.insert(1, 10)
    arr.remove(2)
    assert arr.to_list() == [1, 10, 3]
    assert "DynamicArray" in repr(arr)


def test_stack() -> None:
    stack = Stack[int]([1, 2])
    stack.push(3)
    assert stack.peek() == 3
    assert "top->bottom" in repr(stack)


def test_queue() -> None:
    queue = Queue[str](["x", "y"])
    queue.enqueue("z")
    assert queue.dequeue() == "x"
    assert "front->rear" in repr(queue)


def test_deque() -> None:
    d = Deque[int]([2])
    d.append_left(1)
    d.append_right(3)
    assert d.pop_left() == 1
    assert d.pop_right() == 3


def test_circular_queue() -> None:
    cq = CircularQueue[int](3)
    cq.enqueue(1)
    cq.enqueue(2)
    assert cq.dequeue() == 1
    cq.enqueue(3)
    assert "CircularQueue" in repr(cq)


def test_singly_linked_list() -> None:
    linked = SinglyLinkedList([2, 3])
    linked.prepend(1)
    linked.append(4)
    assert list(linked) == [1, 2, 3, 4]
    assert "SinglyLinkedList" in repr(linked)


def test_doubly_linked_list() -> None:
    linked = DoublyLinkedList([2, 3])
    linked.prepend(1)
    linked.append(4)
    assert linked.pop_front() == 1
    assert linked.pop_back() == 4
    assert list(linked) == [2, 3]
    assert "DoublyLinkedList" in repr(linked)
