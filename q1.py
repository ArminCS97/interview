from typing import List, Dict, Tuple, Union


# The time complexity is O(n == len(edges)) as we iterate over the edges only once and
# the time complexity of dict.setdefault() is O(1). dict uses a hashing mechanism that is
# designed in a way to minimize the number of "collisions" and therefore accessing an
# item in such a structure is in constant time.
def to_tree(edges: List[Tuple[Union[None, str], str]]) -> Union[Dict[str, dict], dict]:
    if len(edges) == 0:
        return {}
    graph = {}
    for parent, child in edges:
        graph.setdefault(parent, {})[child] = graph.setdefault(child, {})
    # Here the assumption is that the root of the tree is None
    if None not in graph:
        raise Exception('The root is assumed to be None and present')
    tree = graph[None]
    return tree


edges1 = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected1 = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

edges2 = [
    (None, 'a'),
    (None, 'b'),
    ('a', 'a1'),
    ('a1', 'a11'),
    ('a11', 'a12'),
    ('a12', 'a13'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2')
]

expected2 = {
    'a': {'a1': {'a11': {'a12': {'a13': {}}}}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}}
}

assert to_tree(edges1) == expected1, 'edges1 != expected1'
assert to_tree(edges2) == expected2, 'edges2 != expected2'
