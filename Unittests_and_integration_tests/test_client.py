#!/usr/bin/env python3
"""
A module for testing the client module.
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos returns the expected list."""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = test_payload

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/test/repos"
            client = GithubOrgClient("test")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with(mock_url.return_value)
            mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license returns the expected boolean."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    A class for testing the GithubOrgClient class in integration.
    """

    @classmethod
    def setUpClass(self):
        """Set up test fixtures before running tests."""
        self.get_patcher = patch('requests.get')
        self.mock_get = self.get_patcher.start()

        def get_patcher(url):
            """Start a patch for requests.get"""
            mock_response = Mock()
            if "orgs/google" in url:
                mock_response.json.return_value = self.org_payload
            elif "repos" in url:
                mock_response.json.return_value = self.repos_payload

    @classmethod
    def tearDownClass(self):
        """Stop the patch for requests.get"""
        self.get_patcher.stop()
