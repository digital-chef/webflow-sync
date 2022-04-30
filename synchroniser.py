from appservice import (
  AppService,
  Query,
  QueryResponse
)

import constants

class GetSchemaResponse(QueryResponse):
  def GetName():
    pass

class GetSchemaQuery(Query):
  def GetResponse() -> GetSchemaResponse:
    pass
  
def main():
  app_service = AppService()
  response: GetSchemaResponse = app_service.Query(GetSchemaQuery())  
  response.GetName()
  print(constants.FROM_WEBFLOW_ACCESS_TOKEN)
  