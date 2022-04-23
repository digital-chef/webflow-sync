from appservice import (
  AppService,
  Query,
  QueryResponse
)

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
  