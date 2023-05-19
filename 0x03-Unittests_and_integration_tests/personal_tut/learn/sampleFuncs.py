#!/usr/bin/env python3
"""Mock function to learn unittesting"""

from typing import Tuple


class Widget():
    """checks for the size of supplied widget and returns it
    """

    def __init__(self, string: str) -> None:
        self.string = string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        if type(value) is not str:
            raise TypeError('must be a string')
        if value == '':
            raise ValueError('please supply valid string as widget')
        self._string = value

    def __str__(self) -> str:
        return self.string

    def size(self) -> Tuple:
        return (len(self._string) * 4, len(self._string) * 4)

    def resize(self) -> Tuple[int, int]:
        old_size = self.size()
        new_size = (old_size[0], old_size[1] + 50)
        return new_size


if __name__ == '__main__':
    test = Widget('I just wrote a class to learn unittesting')
    print(test)
    print(test.size())
    print(test.resize())
