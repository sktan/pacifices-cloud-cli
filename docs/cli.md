# CLI Usage

To use this via CLI, you will need to first setup the credentials. This can be done via the following methods:

Exporting a variable:
```
# exporting variables
export PACIFICES_API_KEY="my_pacifices_cloud_api_key"
```

Using a .env file (located in the directory you're executing the CLI command)
```
# Contents of example .env file
PACIFICES_API_KEY="my_pacifices_cloud_api_key"

[sktan@desktop ~]$ pacifices-cloud create --map de_dust2 --plugin warmod
```

## Creating a Server

Creating a de_dust2 server with warmod pre-installed

```
pacifices-cloud create --map de_dust2 --plugin warmod
```

Creating a de_dust2 server with warmod pre-installed (with pre-configured RCON and server join passwords)

```
pacifices-cloud create --map de_dust2 --plugin warmod --rcon myrconpassword123 --password joinme
```

## Restarting / Destroying / Updating a server

```
# Restart a Server
pacifices-cloud restart --serverid abcd-efgh-ijkl
# Destroy a Server
pacifices-cloud destroy --serverid abcd-efgh-ijkl
# Perform a server Update
pacifices-cloud update --serverid abcd-efgh-ijkl
```
