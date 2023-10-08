from mockito import when, mock, verify

from seminars.fourth.hw.web_service.http_client import HttpClient
from seminars.fourth.hw.web_service.web_service import WebService


class TestWebService:
    def test_request(self):
        url = "http://goodurl.com"
        good_response = "response"
        mock_client = mock(HttpClient)
        when(mock_client).get(url).thenReturn(good_response)
        web_service = WebService(mock_client)

        response = web_service.request(url)

        verify(mock_client, times=1).get(url)
        assert good_response == response
