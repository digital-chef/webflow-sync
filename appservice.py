class Command():
    pass


class Query():
    pass


class QueryResponse():
    pass


class AppService():
    def Query(query: Query) -> QueryResponse:
        pass

    def Execute(command: Command) -> None:
        pass
