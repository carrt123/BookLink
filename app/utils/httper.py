import requests


class Http:
    @staticmethod
    def get(url, return_json=True):
        response = requests.get(url)
        if response.status_code != 200:
            return {} if return_json else ""
        if return_json:
            return response.json()
        return response.text
