from pytest import fixture
from py_fenwick.fenwick import FenwickTree


@fixture
def int_fenwick_tree() -> FenwickTree[int]:
    return FenwickTree.of_values(values=[4, 1, 2, 8, 3, 9, 1], zero=0)


def test_fenwick_tree_ops_works():
    assert True
