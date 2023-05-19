#!/usr/bin/env python3
"""
unit test for utils.access_nested_map.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, param
from utils import access_nested_map as aNm
from utils import get_json as gj
from utils import memoize


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
        '''
        test method for access_nested_map
        '''
        self.assertEqual(aNm(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, err_message):
        '''
        test method for access_nested_map KeyError
        '''
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
        test that when calling a_property twice, the correct result is returned but a_method is only called once using assert_called_once
        '''
        class TestClass:
            '''
            test class that inherits from unittest
            '''

            def a_method(self):
                '''
                test method for a_method
                '''
                return 42

            @memoize
            def a_property(self):
                '''
                test method for a_property
                '''
                return self.a_method()

        test = TestClass()
        with patch.object(test, 'a_method') as mock_a_method:
            test.a_property()
            test.a_property()

            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
