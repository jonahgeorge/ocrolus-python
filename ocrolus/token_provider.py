from datetime import datetime, timedelta
from ocrolus.auth_client import AuthClient

class BearerTokenProvider:
    expires_at: datetime | None
    access_token: str | None

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        auth_client: AuthClient | None = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_client = auth_client or AuthClient()
        self.access_token = None
        self.expires_at = None

    def __call__(self) -> str:
        if (
            self.access_token is None
            or self.expires_at is None
            or self.expires_at < datetime.now()
        ):
            response = self.auth_client.grant_auth_token(
                {
                    "grant_type": "client_credentials",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                }
            )

            self.access_token = str(response["access_token"])
            self.expires_at = datetime.now() + timedelta(seconds=response["expires_in"])

        return self.access_token
