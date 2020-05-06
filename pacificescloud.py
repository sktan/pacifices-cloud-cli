#!/usr/bin/env python
"""
A CLI tool for managing your https://pacifices.cloud servers
"""
import argparse
import inspect
import logging
import os
import json

from pacifices.cloud import server
from dotenv import load_dotenv

def parse_args():
  """ A method to handle parsing of arguments passed when executing via CLI """
  description = inspect.cleandoc(
    """
    A command line interface for managing your https://pacifices.cloud/ servers

    Example usage:
    pacifices-cloud create --name mycsgoserver --map de_dust2 --plugin warmod
    pacifices-cloud destroy --serverid abcdefgh
    pacifices-cloud list --serverid abcd-efgh-ikl --serverid abcd-efgh-mnop
    ------------------------
    https://github.com/sktan/pacifices-cloud-cli
    """
  )
  parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=description
  )
  subparser = parser.add_subparsers(
    dest='action',
    help='Valid actions to perform against https://pacifices.cloud/'
  )

  # Sub parser for creating a CSGO server
  create_parser = subparser.add_parser('create', help='Create a CSGO server')
  create_parser.add_argument('--name', help='Name of your CSGO server', required=True)
  create_parser.add_argument('--map', help='CSGO map (e.g. de_dust2)', default="de_dust2")
  create_parser.add_argument('--tickrate', help='CSGO server tickrate', default=128, choices=[128, 64])
  create_parser.add_argument('--rcon', help='CSGO RCON password (defaults to a random password)')
  create_parser.add_argument('--password', help='CSGO Server Join password')
  # Currently only supports Sydney
  create_parser.add_argument('--location', help='CSGO Server Location', default="Sydney", choices=["Sydney"])
  create_parser.add_argument('--plugin', help='CSGO Plugins', type=str, action='append', choices=["warmod", "nadetails"])

  # Sub parser for destroying a CSGO server
  destroy_parser = subparser.add_parser('destroy', help='Destroy a CSGO server')
  destroy_parser.add_argument('--serverid', help='ServerId of your PacificES Cloud server', required=True)

  # Sub parser for restarting a CSGO server
  restart_parser = subparser.add_parser('restart', help='Restart a CSGO server')
  restart_parser.add_argument('--serverid', help='ServerId of your PacificES Cloud server', required=True)

  # Sub parser for updating a CSGO server
  update_parser = subparser.add_parser('update', help='Update a CSGO server')
  update_parser.add_argument('--serverid', help='ServerId of your PacificES Cloud server', required=True)

  # Sub parser for listing CSGO servers
  update_parser = subparser.add_parser('list', help='Lists your CSGO server')
  update_parser.add_argument('--serverid', help='ServerId of your PacificES Cloud server', type=str, action='append')

  args = parser.parse_args()
  if not args.action:
    parser.print_help()
  return args

def main():
  """ Entrypoint for CLI application """
  args = parse_args()

  load_dotenv()
  cloudserver = server.server(api_key=os.getenv('PACIFICES_API_KEY'))

  if args.action == 'create':
    kwargs = {
      'name': args.name,
      'map': args.map,
      'tickrate': args.tickrate,
      'location': args.location,
      'plugins': args.plugin,
    }
    if args.rcon:
      kwargs['rcon_password'] = args.rcon
    if args.password:
      kwargs['password'] = args.password
    result = cloudserver.create(**kwargs)
  elif args.action == 'restart':
    result = cloudserver.restart(server_id=args.serverid)
  elif args.action == 'destroy':
    result = cloudserver.destroy(server_id=args.serverid)
  elif args.action == 'update':
    result = cloudserver.update(server_id=args.serverid)
  elif args.action == "list":
    result = cloudserver.retrieve(server_ids=args.serverid)
  print(json.dumps(result, indent=2))

if __name__ == "__main__":
  main()
