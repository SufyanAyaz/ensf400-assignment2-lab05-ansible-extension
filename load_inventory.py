import ansible_runner import Runner

def main():
    inven = ansible_runner.Runner(inventory='/workspaces/ensf400-assignment2-lab05-ansible-extension/hosts.yml').run(inventory_only=True)

    for host in inven.inventory.list_hosts():
        


if __name__ == "__main__":
    main()