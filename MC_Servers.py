from mcstatus import JavaServer
import random, os, sys

filename = 'servers.csv'
separator = '-' * 30
port = 25565 # the default port

# it runs forever until you close the window
while True:
    # generate an IP address
    # the first number is different because some at the beginning and end are reserved and can't be used for public IPs
    ip = [random.randrange(1, 239), random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]
    ip_string = f'{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}'

    # generate a random port if enabled
    # turning this on will decrease your odds of finding a server, but it'll allow you to find more than just those that use the default port
    if '-p' in sys.argv:
        port = random.randrange(1024, 65535)

    # skip reserved ranges
    # this line of code is massive and I honestly dont know if it works properly
    if ip[0] in [10, 127] or (ip[0] == 100 and (ip[1] >= 64 and ip[1] <= 127)) or (ip[0] == 169 and ip[1] == 254) or (ip[0] == 172 and (ip[1] >= 16 and ip[1] <= 31)) or (ip[0] == 192 and ((ip[1] == 0 and ip[2] in [0, 2]) or (ip[1] == 31 and ip[2] == 196) or (ip[1] == 52 and ip[2] == 193) or (ip[1] == 88 and ip[2] == 99) or ip[1] == 128 or (ip[1] == 175 and ip[2] == 48))) or (ip[0] == 198 and ((ip[1] >= 18 and ip[1] <= 19)) or (ip[1] == 51 and ip[2] == 100)) or (ip[0] == 203 and ip[1] == 0 and ip[2] == 113):
        continue

    # tell the user the IP is being checked
    print(f'Checking {ip_string}:{port}')

    # lookup the Minecraft server
    server = JavaServer.lookup(f'{ip_string}:{port}')

    # check if the server exists by gettings its status
    # if it doesnt exist the program will try to crash
    # maybe there's a better way to implement this, but idk what that is so here you go
    try:
        status = server.status()
    except:
        # tell the user the check failed
        print('Check failed')

        # go on to the next one
        continue

    # tell the user a server was found
    print('Server found!')

    # print all of the server's information
    print(f'{separator}\nServer IP: {ip_string}\nVersion: {status.version.name}\nLatency: {round(status.latency)}ms\nPlayers: {"{:,}".format(status.players.online)}\nDescription:\n{status.description}\n{separator}')

    print('Adding server to spreadsheet...')

    # check if the spreadsheet exists
    if os.path.exists(filename):
        # it exists, so lets just add to it
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f'\n"{ip_string}","{status.version.name}","{round(status.latency)}","{status.players.online}","{status.description}"')
    else:
        # it doesnt exist, so lets create a new file with a header
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'"Server IP","Version","Latency","Players","Description"\n"{ip_string}","{status.version.name}","{round(status.latency)}","{status.players.online}","{status.description}"')

    print('Server added to spreadsheet.')