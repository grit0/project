import commands
#commands.getoutput('git clone https://github.com/grit0/sta.git')
status=commands.getoutput('date')
with open("./sta/iffile", "w") as file:
	file.write(status)
commands.getoutput('./shell.sh')
#commands.getoutput('sudo git commit -am "p1" &&  git push origin master')
