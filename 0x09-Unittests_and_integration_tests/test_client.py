#!/usr/bin/env python3

""" Tests for client
"""

import unittest
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock
from utils import get_json
from client import GithubOrgClient
import client


class TestGithubOrgClient(unittest.TestCase):
    """ Test class for GithubOrgClient
    """

    @parameterized.expand(
        [("google", {"google", True}), ("abc", {"abc", True})])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """ Test the GithubOrgClient.org method
        """
        get_patch.return_value = expected
        gh_client = GithubOrgClient(org)
        self.assertEqual(gh_client.org, expected)
        get_patch.assert_called_once_with(f'https://api.github.com/orgs/{org}')

    def test_public_repos_url(self):
        """ Test the GithubOrgClient._public_repos_url
        """
        expected = "www.geoff.com"
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value={'repos_url': expected})):
            gh_client = GithubOrgClient("adobe")
            self.assertEqual(gh_client._public_repos_url, expected)
