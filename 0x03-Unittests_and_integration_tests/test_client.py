#!/usr/bin/env python3
"""
Parameterize and patch as decorators,
Mocking a property, More patching,
Parameterize, Integration test: fixtures, Integration tests
"""

import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, param
from client import GithubOrgClient as GOC
from typing import Mapping, Sequence, Any


class TestGithubOrgClient(unittest.TestCase):
    '''test class that inherits from unittest'''

    @parameterized.expand([
        param(org='google'),
        param(org='abc'),
    ])
    @patch('client.get_json')
    def test_org(self, get_mock: MagicMock, org: str):
        '''
        test that GithubOrgClient.org returns the correct value
        '''
        goc = GOC(org)
        goc.org()
        get_mock.assert_called_once_with('https://api.github.com/orgs/' + org)

    def test_public_repos_url(self):
        '''
        test that the result of _public_repos_url is the expected one based on the mocked payload
        '''
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value = 'http://some_url'
            goc = GOC('test')
            self.assertEqual(goc._public_repos_url,
                             'http://some_url')
            mock_url.assert_called_once_with()

    @patch('client.get_json')
    def test_public_repos(self, get_mock: MagicMock) -> None:
        '''
        unit test for GithubOrgClient.public_repos
        '''
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:

            mock_url.return_value = 'http://some_url'
            get_mock.return_value = [{'name': 'google'}, {'name': 'abc'}]
            goc = GOC('test')

            self.assertEqual(goc.public_repos(), ['google', 'abc'])
            mock_url.assert_called_once_with()
            get_mock.assert_called_once_with('http://some_url')

    @parameterized.expand([
        param(input_payload={'license': {'key': 'my_license'}},
              expected_license_key='my_license'),
        param(input_payload={'license': {'key': 'other_license'}},
              expected_license_key='other_license'),
    ])
    def test_has_license(self, input_payload: Mapping[str, Any], expected_license_key: str) -> None:
        '''
        unit test for GithubOrgClient.has_license
        '''
        goc = GOC('test')
        self.assertEqual(goc.has_license(
            input_payload, expected_license_key), True)
