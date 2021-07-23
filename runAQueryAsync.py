import asyncio

async def execute(connection, query):
     results = connection.execute(query)
     return results

async def executeQuery(query: str, connectionParams:dict):
     conn = getConnection(connectionParams.get('host'), connectionParams.get('username'), connectionParams.get('password'))
     results = await execute(conn, query)
     #computation on top of returned results
     return results


allResults = [executeQuery("select * from table where col1=1", {}),
executeQuery("select * from table1 where col2=1", {})]


#on top of allresults, some logic would be there