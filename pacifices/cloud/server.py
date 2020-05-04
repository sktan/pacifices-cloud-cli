"""
A class to handle management of https://pacifices.cloud servers
"""
import typing
import requests
import json

class server(object):
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
  
  def __api_endpoint(self, route):
    r"""Return the API endpoint relevant to the action we are performing

    Args:
      route (str): The route of the action we are looking to perform e.g. servers
    
    Returns:
      str: A fully built URI e.g. https://api.pacifices.cloud/v1/servers
    """
    return "{:s}{:s}".format(self.__api_url_base, route)

  def create(self, name: str,
    password: typing.Optional[str]=None,
    rcon_password: typing.Optional[str]=None,
    gamemode: str="Competitive",
    location: str="Sydney",
    map: str="de_dust2",
    plugins: list=["warmod"],
    tickrate: int=128,
  ):
    raise NotImplementedError

  def retrieve(self,
    server_ids: typing.Optional[list],
    status: str="running"
  ) -> list:
    raise NotImplementedError

  def destroy(self, server_id: str) -> dict:
    raise NotImplementedError

  def update(self, server_id: str) -> dict:
    raise NotImplementedError

  def restart(self, server_id: str) -> dict:
    raise NotImplementedError

  def send_command(self, server_id: str, command: str) -> dict:
    raise NotImplementedError

  def version(self, server_id: str) -> dict:
    raise NotImplementedError
