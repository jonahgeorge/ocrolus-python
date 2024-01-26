from requests import Response, post
from typing import TypedDict
from typing_extensions import NotRequired, Required


class GrantAuthTokenRequest(TypedDict):
    """
    https://docs.ocrolus.com/reference/grant-authentication-token
    """

    grant_type: Required[str]
    """
    The OAuth 2.0 grant type for the returned token. Must have a value of client_credentials, as we don't offer other grant types at this time.

    Default: `client_credentials`
    """

    audience: NotRequired[str]
    """
    The domain in which the token will be used. We currently only support the value of https://api.ocrolus.com/ (including the trailing /).
    """

    client_id: Required[str]
    """
    The client ID that was generated from the Ocrolus Dashboard.
    """

    client_secret: Required[str]
    """
    The client secret associated with the client ID that was generated from the Ocrolus Dashboard.
    """


class AuthClient:
    """
    A client for the Ocrolus Auth API.

    https://docs.ocrolus.com/reference/ocrolus-api-intro
    """

    def __init__(self, base_url: str = "https://auth.ocrolus.com"):
        self.base_url = base_url

    def _headers(self):
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def grant_auth_token(self, req: GrantAuthTokenRequest) -> Response:
        """
        Retrieve a JWT-compliant access token for use with all other endpoints.

        https://docs.ocrolus.com/reference/grant-authentication-token
        """

        return post(f"{self.base_url}/oauth/token", headers=self._headers(), json=req)
