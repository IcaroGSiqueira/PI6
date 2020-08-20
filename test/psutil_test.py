import psutil #sudo apt install python3-psutil

temp = psutil.sensors_temperatures(fahrenheit=False)

fan = psutil.sensors_fans()

batt = psutil.sensors_battery()

print(temp)
print(fan)
print(batt)

#names = list(temp.keys())
#for entry in temp[names[0]]:
	#print("%s %s°C" % (entry.label, entry.current))
#	break
#cpu_temp = entry.current
#print(cpu_temp)