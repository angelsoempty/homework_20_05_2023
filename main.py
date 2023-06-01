import requests
class InvalidUrlError(Exception):
    def __init__(self, url):
        self.url = url
        super().__init__(f"Invalid URL: {url}")
def fetch_data_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise InvalidUrlError(url)
        return response.text
    except requests.exceptions.RequestException:
        raise InvalidUrlError(url)

url = "https://example.com/invalid"
try:
    data = fetch_data_from_url(url)
    print(data)
except InvalidUrlError as e:
    print(e)
