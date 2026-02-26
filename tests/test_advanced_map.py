from dscollections import DisjointSet, HashMap, HashSet, Trie


def test_hash_map_and_set() -> None:
    m = HashMap[str, int]()
    m.put("a", 1)
    m.put("b", 2)
    assert m.get("a") == 1
    assert "HashMap" in repr(m)

    s = HashSet[int]()
    s.add(1)
    s.add(2)
    assert s.contains(2)
    assert "HashSet" in repr(s)


def test_trie() -> None:
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    assert trie.search("app")
    assert trie.starts_with("ap")
    assert "Trie" in repr(trie)


def test_disjoint_set() -> None:
    dsu = DisjointSet[int]()
    dsu.union(1, 2)
    dsu.union(2, 3)
    assert dsu.connected(1, 3)
    assert "groups" in repr(dsu)
