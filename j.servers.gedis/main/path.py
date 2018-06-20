from JumpScale9 import j



def api_meta(request, namespace, dbclient):
    '''
    return the api meta information



    '''
    return a+b
    



def core_schemas_get(request, namespace, dbclient):
    '''
    return all core schemas as understood by the server, is as text, can be processed by j.data.schema



    '''
    return a+b
    



def get(request, namespace, dbclient):
    '''
    This is the basis for the generation of the template code. request,namespace and dbclient will be added in the template after server start.
request is the data from the command.
dbclient is the client used to connect to the backend.

    '''
    if len(request) > 2:
        raise j.exceptions.RuntimeError('Unsupported command arguments')
    import asyncio
    loop = asyncio.get_event_loop()
    task = asyncio.async(dbclient.get(namespace, request[1].decode("utf-8")))
    return loop.run_until_complete(task)
    



def ping(request, namespace, dbclient):
    return "PONG"
    



def set(request, namespace, dbclient):
    '''
    This is the basis for the generation of the template code. request,namespace and dbclient will be added in the template after server start.
request is the data from the command.
dbclient is the client used to connect to the backend.

    '''
    if len(request) > 3:
        raise j.exceptions.RuntimeError('Unsupported command arguments')
    import asyncio
    loop = asyncio.get_event_loop()
    task = asyncio.async(dbclient.put(namespace, **{request[1].decode("utf-8"): request[2].decode("utf-8")}))
    return loop.run_until_complete(task)
    

