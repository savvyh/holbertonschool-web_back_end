#!/usr/bin/env python3
"""
A module for testing the client module.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    A class for testing the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org returns the correct value."""
        url = f"https://api.github.com/orgs/{org_name}"
        test_payload = {"name": org_name, "repos_url": url}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, test_payload)
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url returns the expected URL."""
        url = "https://api.github.com/orgs/test/repos"
        test_payload = {"repos_url": url}

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload
            client = GithubOrgClient("test")
            result = client._public_repos_url

            self.assertEqual(result, url)
