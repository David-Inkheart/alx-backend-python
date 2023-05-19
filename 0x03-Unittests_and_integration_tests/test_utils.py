#!/usr/bin/env python3
"""
unit test for utils.access_nested_map.
"""

import unittest
from parameterized import parameterized, param
from utils import access_nested_map as aNm


class TestAccessNestedMap(unittest.TestCase):
    '''
    test class that inherits from unittest
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        self.assertEqual(aNm(nested_map, path), result)


if __name__ == '__main__':
    unittest.main()
