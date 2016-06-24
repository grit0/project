
import io,json
import commands
basic={
		"Hostname" : "hostname -b",
		"Distro Name":"uname -s",
		"Kernel Version":"uname -v",
		"Date":"date",
		"Machine":"uname -m",
		"Voltage":"vcgencmd measure_volts core",
		"Temperature":"vcgencmd measure_temp"

}
network={
                                                                                                                                                                        
			x:{
				"IP address" : "/sbin/ifconfig "+x+" | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'",
				"IP loopback": "hostname -i",
				"Broadcast"  : "/sbin/ifconfig "+x+" | grep 'inet addr:' | cut -d: -f3 | awk '{ print $1}'",
				"Subnetmask" : "/sbin/ifconfig "+x+" | grep 'inet addr:' | cut -d: -f4 | awk '{ print $1}'",
				"MAC"		 :"/sbin/ifconfig "+x+" | grep 'HWaddr' | tr -s ' ' |cut -d' ' -f5",
				"RX packet"  :"/sbin/ifconfig "+x+" | grep 'RX packet' | cut -d: -f2 | awk '{ print $1}'",
				"TX packet"  :"/sbin/ifconfig "+x+" | grep 'TX packet' | cut -d: -f2 | awk '{ print $1}'",
				"RX bytes"   :"/sbin/ifconfig "+x+" | grep 'RX bytes' | cut -d: -f2 | awk '{ print $1$2$3}'",
				"TX bytes"	 :"/sbin/ifconfig "+x+" | grep 'TX bytes' | cut -d: -f2 | awk '{ print $1$2$3}'"
				} for x in ("eth0","lo")
			# "":"",
}
#print(commands.getoutput(basic["Date"]))
for key, value in basic.items():
	basic[key]=commands.getoutput(basic[key])
#print(basic)

for key, value in network["eth0"].items():
	network["eth0"][key]=commands.getoutput(network["eth0"][key])

status=[basic,network]
with open('sta/j.json', 'w') as file:
	json.dump(basic, file)
#with io.open('data.txt', 'w', encoding='utf-8') as f:
#	f.write(unicode(json.dump(data, ensure_ascii=False)))
#	file.write(string(basic))
#print(commands.getoutput(basic["Date"]))
#for key, value in basic.items():
# 	basic[key]=commands.getoutput(basic[key])
#print(basic)

#for key, value in network["eth0"].items():
#        network["eth0"][key]=commands.getoutput(network["eth0"][key])
#print(network["eth0"])

