import collections.abc
from typing import Union, overload

numeric = Union[int, float]

def floor(value: numeric, size: int, offset: int = 200): ...

class vector(collections.abc.Sequence):
    def __init__(self, x: numeric, y: numeric): ...
    @property
    def x(self): ...
    @x.setter
    def x(self, value: numeric): ...
    @property
    def y(self): ...
    @y.setter
    def y(self, value: numeric): ...
    def __hash__(self) -> int: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int): ...
    @overload
    def __getitem__(self, index: slice): ...
    def copy(self) -> vector: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __iadd__(self, other: Union[vector, numeric]) -> vector: ...
    def __add__(self, other: Union[vector, numeric]) -> vector: ...

    __radd__ = __add__

    def move(self, other: vector) -> None: ...
    def __isub__(self, other: Union[numeric, vector]) -> vector: ...
    def __sub__(self, other: Union[numeric, vector]) -> vector: ...
    def __imul__(self, other: Union[numeric, vector]) -> vector: ...
    def __mul__(self, other: Union[numeric, vector]) -> vector: ...

    __rmul__ = __mul__

    def scale(self, other: Union[numeric, vector]) -> None: ...
    def __itruediv__(self, other: Union[numeric, vector]) -> vector: ...
    def __truediv__(self, other: Union[numeric, vector]) -> vector: ...
    def __neg__(self) -> vector: ...
    def __abs__(self) -> numeric: ...
    def rotate(self, angle: numeric) -> None: ...
    def __repr__(self) -> str: ...
