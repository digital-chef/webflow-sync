import requests
import constants


class Command():
    pass


class Query():
    def __init__(self) -> None:
        pass


class QueryResponse():
    def __init__(self, response_json) -> None:
        self.json = response_json


class HttpAppService():
    def query(self, query: Query) -> QueryResponse:
        token = constants.FROM_WEBFLOW_ACCESS_TOKEN
        headers = {
            'Authorization': f'Bearer {token}',
            'accept-version': '1.0.0'
        }

        response = requests.get(query.url, headers=headers)

        return QueryResponse(response.json())

    def execute(self, command: Command) -> None:
        pass
