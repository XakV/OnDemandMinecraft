import requests

def choose_server_type():
    # Choose Forge or Paper or Vanilla
    # Choose Version
    return

def create_basic_server(server_requirements):
    # use ansible podman here?
    # check to make sure server doesn't exist
    # get a name
    return

def add_mods_and_configure(server):
    # needs a file share or links
    return

def add_server_to_backups(server):
    # use restic
    return

def add_server_to_web_app(server):
    # flask in a container
    return

def run_first_startup(server):
    # whitelists, ops, mod integrity
    # let user know if error or server ready
    return
