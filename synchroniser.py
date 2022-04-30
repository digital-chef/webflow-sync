from appservice import (
    HttpAppService,
    Query,
    QueryResponse
)

import constants
import pprint


class GetSchemaResponse(QueryResponse):
    pass


class GetCollectionsQuery(Query):

    def __init__(self, site_id) -> None:
        self.site_id: int = site_id
        self.url: str = f'https://api.webflow.com/sites/{site_id}/collections'
        super().__init__()

    def get_response(self) -> GetSchemaResponse:
        pass


def main():
    site_id = constants.FROM_WEBFLOW_SITE_ID
    app_service = HttpAppService()
    get_collections_query = GetCollectionsQuery(site_id)
    response: GetSchemaResponse = app_service.query(get_collections_query)
    pprint.pprint(response.json)


if __name__ == "__main__":
    main()
