import os
import requests


class Wunderlist():

    def __init__(self):
        self._wunder_client_id = os.environ["WUNDER_CLIENT_ID"]
        self._wunder_client_secret = os.environ["WUNDER_CLIENT_SECRET"]
        self._wunder_access_token = os.environ["WUNDER_ACCESS_TOKEN"]

        self._wunder_url = os.environ["WUNDER_URL"]

        self._wunder_daglig = os.environ["WUNDER_DAGLIG"]

    def get_list(self):
        response = requests.get(
            f'{self._wunder_url}/lists/{self._wunder_daglig}',
            headers={
                'X-Access-Token': self._wunder_access_token,
                'X-Client-ID': self._wunder_client_id,
            },
        )
        print(response)
        print(response.json())
        for w_list in response.json():
            print('=' * 50)
            print(w_list['id'])
            print(w_list['title'])
        return 'rai'

    def get_tasks(self):
        response = requests.get(
            f'{self._wunder_url}/tasks',
            params={'list_id': self._wunder_daglig},
            headers={
                'X-Access-Token': self._wunder_access_token,
                'X-Client-ID': self._wunder_client_id,
            },
        )
        json_response = response.json()
        return json_response
