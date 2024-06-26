from dataclasses import dataclass
from typing import final, Protocol, TypeVar, Generic, List, TypeAlias, Self


class SupportsFenwick(Protocol):
    def __add__(self, __o: Self) -> Self:
        ...

    def __sub__(self, __o: Self) -> Self:
        ...


Index: TypeAlias = int
T = TypeVar("T", bound=SupportsFenwick)


@final
@dataclass
class FenwickTree(Generic[T]):
    zero: T
    bit: List[T]
    size: int

    @classmethod
    def zeroed_of_size(cls, size: int, zero: T) -> Self:
        return cls(zero=zero, bit=[zero for _ in range(size)], size=size)

    @classmethod
    def of_values(cls, values: List[T], zero: T) -> Self:
        ft = cls.zeroed_of_size(size=len(values), zero=zero)
        for idx, v in enumerate(values):
            ft.add(idx=idx, delta=v)
        return ft

    def prefix_sum(self, right_inclusive: Index) -> T:
        i: Index = right_inclusive
        s: T = self.zero
        while i >= 0:
            s += self.bit[i]
            i = (i & (i + 1)) - 1
        return s

    def range_sum(self, left_inclusive: Index, right_inclusive: Index) -> T:
        return self.prefix_sum(right_inclusive) - self.prefix_sum(left_inclusive - 1)

    def add(self, idx: Index, delta: T):
        i: Index = idx
        while i < self.size:
            self.bit[i] += delta
            i = i | (i + 1)
