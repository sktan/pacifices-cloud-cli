# Library Usage

The library can be used once you have installed the PIP `pacifices-cloud` library.

## Creating a Server
```
>>> from pacifices.cloud import server as pacificescloud
>>> cloudserver = pacificescloud.server(api_key='MY_SECRET_PACIFICES_CLOUD_KEY')
>>> result = cloudserver.create(name="scrimserver", map="de_dust2")
>>> print(result)
{
  "success": true,
  "error": false,
  "result": {
    "id": "my_pacifices_server_id"
  }
}
```

## Restarting a Server
```
>>> from pacifices.cloud import server as pacificescloud
>>> cloudserver = pacificescloud.server(api_key='MY_SECRET_PACIFICES_CLOUD_KEY')
>>> result = cloudserver.restart(serverid="my_pacifices_server_id")
>>> print(result)
{
  "success": true,
  "error": false,
  "result: null
}
```

## Destroying a Server
```
>>> from pacifices.cloud import server as pacificescloud
>>> cloudserver = pacificescloud.server(api_key='MY_SECRET_PACIFICES_CLOUD_KEY')
>>> result = cloudserver.destroy(serverid="my_pacifices_server_id")
>>> print(result)
{
  "success": true,
  "error": false,
  "result: null
}
```

## Updating a Server
```
>>> from pacifices.cloud import server as pacificescloud
>>> cloudserver = pacificescloud.server(api_key='MY_SECRET_PACIFICES_CLOUD_KEY')
>>> result = cloudserver.update(serverid="my_pacifices_server_id")
>>> print(result)
{
  "success": true,
  "error": false,
  "result: null
}
```
