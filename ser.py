import commands
from socket import *
server=socket(AF_INET, SOCK_STREAM)
server.bind(('192.168.1.171',5000))
server.listen(5)
#status="ifconfig"

while True:
	commands.getoutput('git clone https://github.com/grit0/sta.git')
	status=commands.getoutput('ifconfig')
	with open("./sta/iffile", "w") as file:
		file.write(status)
	print('wait....')
	client, address=server.accept()
	print("from : ",address)
	client.send(str.encode(status))
	client.close()
