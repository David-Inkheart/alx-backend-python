#!/usr/bin/env python3
"""
unit test for utils.access_nested_map.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, param
from utils import access_nested_map as aNm
from utils import get_json as gj
from utils import memoize as memo


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

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, err_message):
        with self.assertRaises(KeyError) as e:
            aNm(nested_map, path)
        self.assertEqual(str(e.exception), err_message)


class TestGetJson(unittest.TestCase):
    '''
    test class that inherits from unittest
    '''
    @parameterized.expand([
        param('http://example.com', {'payload': True}),
        param('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, test_url, test_payload):
        '''
        test method for get_json
        '''
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            self.assertEqual(gj(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''
    test class that inherits from unittest
    '''

    def test_memoize(self):
        '''
        test method for memoize
        '''
        class TestClass:
            '''
            test class for memoize
            '''

            def a_method(self):
                '''
                test method for memoize
                '''
                return 42

            @memo
            def a_property(self):
                '''
                test method for memoize
                '''
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
