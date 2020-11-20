#!/usr/bin/env python3

""" Tests for client
"""

import unittest
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import get_json
from client import GithubOrgClient, org


class TestGithubOrgClient(unittest.TestCase):
    """ Test class for GithubOrgClient
    """

    @patch('client.get_json')
    @parameterized.expand(
        [("google", {"google", True}), ("abc", {"abc", True})])
    def test_org(self, org, expected, patch):
        """ Test the GithubOrgClient.org method
        """
        patch.return_value = expected
        gh_client = GithubOrgClient(org)
        self.assertEqual(gh_client.org, expected)
        patch.assert_called_once_with(f'https://api.github.com/orgs/{org}')
