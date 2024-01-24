from ocrolus.auth_client import AuthClient
from ocrolus.token_provider import BearerTokenProvider
from unittest.mock import MagicMock
from unittest import TestCase


class BearerTokenProviderTest(TestCase):
    def test_token(self):
        auth_client = AuthClient()
        auth_client.grant_auth_token = MagicMock(
            return_value={
                "access_token": "faketoken",
                "expires_in": 5,
            }
        )

        provider = BearerTokenProvider("", "", auth_client=auth_client)

        self.assertEqual(provider(), "faketoken")
        self.assertEqual(provider(), "faketoken")

        auth_client.grant_auth_token.assert_called_once()
