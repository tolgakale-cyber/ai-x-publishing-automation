import os


class XConnector:
    def __init__(self):
        self.api_key = os.getenv("X_API_KEY")
        self.api_secret = os.getenv("X_API_SECRET")
        self.access_token = os.getenv("X_ACCESS_TOKEN")
        self.access_token_secret = os.getenv(
            "X_ACCESS_TOKEN_SECRET"
        )

    def credentials_configured(self):
        credentials = [
            self.api_key,
            self.api_secret,
            self.access_token,
            self.access_token_secret,
        ]

        return all(credentials)

    def connection_status(self):
        if self.credentials_configured():
            return {
                "platform": "X",
                "configured": True,
                "status": "READY_FOR_LIVE_CONNECTION",
            }

        return {
            "platform": "X",
            "configured": False,
            "status": "DRY_RUN_ONLY",
        }

    def publish(self, post):
        if not self.credentials_configured():
            return {
                "success": False,
                "reason": "X API credentials are not configured.",
            }

        return {
            "success": False,
            "reason": (
                "Live X API execution is intentionally disabled "
                "in this portfolio build."
            ),
            "content": post,
        }