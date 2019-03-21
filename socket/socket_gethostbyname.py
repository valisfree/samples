import socket
HOSTS = ['gift', 'pymotw.com', 'www.python.org', 'wrongname']

for host in HOSTS:
    print(host)
    try:
        print("function gethostbyname")
        print('\t', '{} : {}'.format(host, socket.gethostbyname(host)))
        print("function gethostbyname_ex")
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print("\tHostname: ", name)
        print("\tAliases: ", aliases)
        print("\tAddresses: ", addresses)
    except socket.error as msg:
        print('{} : {}'.format(host, msg))
    print()
