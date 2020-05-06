"""
A class to handle management of https://pacifices.cloud servers
"""
import typing
import secrets
import json
import requests

class server():
  """ A class to handle management of https://pacifices.cloud servers """
  __api_key = None
  __api_url_base = "https://api.pacifices.cloud/v1/"

  def __init__(self, api_key: str) -> None:
    r"""Initialise the PacificES cloud server management class

    NOTE: An API key will be required which can be generated via https://pacifices.cloud/

    Args:
      api_key: A PacificES.cloud API key
    """
    self.__api_key = api_key
  
  def __api_endpoint(self, route: str):
    r"""Return the API endpoint relevant to the action we are performing

    Args:
      route (str): The route of the action we are looking to perform e.g. servers

    Returns:
      str: A fully built URI e.g. https://api.pacifices.cloud/v1/servers
    """
    return "{:s}{:s}".format(self.__api_url_base, route.strip("/"))

  def __api_request(self, route: str, data: typing.Optional[dict]=None, http_type: str="GET"):
    r"""Sends an API request to the specified route using the given data parameter

    Args:
      route      (str): The route of the action we are looking to perform e.g. servers
      data      (dict): The data sent with the the API request
      http_type  (str): The type of HTTP request to send (GET, POST, DELETE, PUT)

    Returns:
      dict: Data returned from the API consisting of the JSON response

    Examples:
      >>> self.__api_request("servers/abcd-efgh-ijkl", http_type: "DELETE")
      {
        "success": true,
        "error": false,
        "result": null
      }
    """
    endpoint = self.__api_endpoint(route)
    headers = {
      "Authorization": self.__api_key,
      "Content-Type": "application/json"
    }
    if http_type == "GET":
      response = requests.get(
        endpoint,
        headers=headers,
        params=data
      )
    elif http_type == "POST":
      response = requests.post(
        endpoint,
        headers=headers,
        data=data
      )
    elif http_type == "PUT":
      response = requests.put(
        endpoint,
        headers=headers,
        data=data
      )
    elif http_type == "DELETE":
      response = requests.delete(
        endpoint,
        headers=headers
      )
    return response.json()

  def create(self, name: str,
    password: typing.Optional[str]=None,
    rcon_password: typing.Optional[str]=None,
    gamemode: str="competitive",
    location: str="Sydney",
    map: str="de_dust2",
    plugins: list=["warmod"],
    tickrate: int=128,
  ):
    r"""Create a PacificES Cloud server

    Args:
      name (str): The name of the game server
      password (str, optional): A server join password
      rcon_password (str, optional): A server RCON password (if unspecified, a random 16 character one will be generated)
      gamemode (str): The Gamemode to start our server in
      location (str): Location of the CSGO server (Currently only supports Sydney)
      map (str): CSGO server map (e.g. de_dust2)
      plugins (str): CSGO plugins to include (e.g. Warmod, nadetails)
      tickrate (int): CSGO server tickrate (128, 64)

    Returns:
      dict: A JSON response converted into dictionary form from the API indicating a success or failure
      {
        "success": true,
        "error": false,
        "result": {
          "id": "abcd-efgh-ijkl"
        }
      }
    """
    # Generate a random 16 character RCON password if none specified
    if not rcon_password:
      rcon_password = secrets.token_urlsafe(16)
    creation_data = {
      "name": name,
      "gamemode": gamemode,
      "map": {
        "type": "default",
        "id": map,
        "group": "mg_active"
      },
      "rcon": rcon_password,
      "plugins": plugins,
      "tickrate": tickrate,
      "location": {
        "city": location
      }
    }
    # Setup a password if one is included
    if password:
      creation_data['password'] = {
        "enabled": True,
        "value": password
      }
    return self.__api_request(route="servers", data=json.dumps(creation_data), http_type="POST")

  def retrieve(self,
    server_ids: typing.Optional[list],
    status: str="running"
  ) -> list:
    r"""Retrieve a list of CSGO servers

    Args:
      server_ids (list, optional): A specific list of CSGO servers we want to retrieve (empty = all)
      status (str): The status of the servers we want to retrieve

    Returns:
      dict: A JSON response converted into dictionary form from the API indicating a success or failure
      {
        "success": true,
        "error": false,
        "result": [
          {
            "id": "abcd-efgh-ijkl",
            "name": "MyTestServer",
            "map": {
              "group": "mg_active",
              "id": "de_cache",
              "name": "de_cache",
              "type": "default"
            },
            "cost": 95,
            "created": 1486386447,
        ....
      }
    """
    data = {
      "status": status
    }
    results = self.__api_request("servers", data=data)
    if server_ids:
      filtered_results = {
        "success": results['success'],
        "error": results['error'],
        "result": []
      }
      for result in results['result']:
        if result['id'] in server_ids:
          filtered_results['result'].append(result)
      results = filtered_results
    return results

  def destroy(self, server_id: str) -> dict:
    """Destroy a CSGO server

    Args:
      server_id (str): The PacificES Cloud serverid to destroy

    Returns:
      dict: A JSON response converted into dictionary form from the API indicating a success or failure
      {
        "success": true,
        "error": false,
        "result": null
      }
    """
    return self.__api_request(route="servers/{:s}".format(server_id), http_type="DELETE")

  def update(self, server_id: str) -> dict:
    """Update a CSGO server to the latest version

    Args:
      server_id (str): The PacificES Cloud serverid to update

    Returns:
      dict: A JSON response converted into dictionary form from the API indicating a success or failure
      {
        "success": true,
        "error": false,
        "result": null
      }
    """
    return self.__api_request(route="servers/{:s}/update".format(server_id), http_type="POST")

  def restart(self, server_id: str) -> dict:
    """Restart a CSGO server

    Args:
      server_id (str): The PacificES Cloud serverid to restart

    Returns:
      dict: A JSON response converted into dictionary form from the API indicating a success or failure
      {
        "success": true,
        "error": false,
        "result": null
      }
    """
    return self.__api_request(route="servers/{:s}/restart".format(server_id), http_type="POST")

  def send_command(self, server_id: str, command: str) -> dict:
    """Sends a RCON command to the CSGO server
    
    Args:
      server_id (str): The PacificES Cloud serverid to receive command
      command (str): A command to send

    Returns:
      dict: A JSON response converted into dictionary form from the API indicating a success or failure
      {
        "success": true,
        "error": false,
        "result": null
      }
    """
    return self.__api_request(
      route="servers/{:s}/command".format(server_id),
      data=json.dumps(
        {
          "command": command
        }
      ),
      http_type="POST"
    )

  def version(self, server_id: str) -> dict:
    """Retrieve the current running version of the given CSGO server

    Args:
      server_id (str): The PacificES Cloud serverid to check version

    Returns:
      dict: A JSON response converted into dictionary form from the API with a CSGO server version
      {
        "server_version": "1.35.6.6",
        "node_version": "1.35.6.6",
        "server_out_of_date": false
      }
    """
    return self.__api_request(route="servers/{:s}/version".format(server_id))
