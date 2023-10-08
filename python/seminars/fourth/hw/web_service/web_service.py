from seminars.fourth.hw.web_service.http_client import HttpClient


class WebService:
    def __init__(self, http_client: HttpClient):
        self._client = http_client

    def request(self, url: str) -> str:
        return self._client.get(url)
