from fabric import Connection, task


@task
def fab_test():
    c = Connection(host="ohendarko@DESKTOD", connect_kwargs= {"password": "subm()r1n3"})
    result = c.run("whoami")
    print(f"Ran command: {result.command!r}, on {result.connection.host} with result: {result.stdout}")
