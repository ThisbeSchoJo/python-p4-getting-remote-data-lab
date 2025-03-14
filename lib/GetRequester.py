import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # sends a GET request to the URL passed in on initialization
        # should return the body of the response
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # should use get_response_body to send a request
        # then returns a Python list or dictionary made up of data converted from the response of that request
        response_body = self.get_response_body()
        return json.loads(response_body)