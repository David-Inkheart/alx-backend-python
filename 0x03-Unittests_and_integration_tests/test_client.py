#!/usr/bin/env python3
"""
unit test for utils.access_nested_map.
"""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, param
from utils import access_nested_map as aNm
from utils import get_json as gj
from utils import memoize as memo
from client import GithubOrgClient as GOC
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''
    test class that inherits from unittest
    '''
    @parameterized.expand([
        param(org='google'),
        param(org='abc'),
    ])
    @patch('client.get_json')
    def test_org(self, get_mock, org):
        '''
        test method for org
        '''
        goc = GOC(org)
        goc.org()
        get_mock.assert_called_once_with('https://api.github.com/orgs/' + org)

    def test_public_repos_url(self):
        '''
        test method for _public_repos_url
        '''
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'http://some_url'}
            goc = GOC('test')
            self.assertEqual(goc._public_repos_url, 'http://some_url')
            mock_org.assert_called_once_with()

    @patch('client.get_json')
    def test_public_repos(self, get_mock):
        '''
        test method for public_repos
        '''
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value = 'http://some_url'
            get_mock.return_value = [{'name': 'google'}, {'name': 'abc'}]
            goc = GOC('test')
            self.assertEqual(goc.public_repos(), ['google', 'abc'])
            mock_url.assert_called_once_with()
            get_mock.assert_called_once_with('http://some_url')
