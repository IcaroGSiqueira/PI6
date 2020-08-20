from pyspectator.computer import Computer
from pyspectator.processor import Cpu
from time import sleep

computer = Computer()
computer.os

#print(computer.python_version)

#print(computer.uptime)

#print(computer.processor.name)

cpu = Cpu(monitoring_latency=1)

with cpu:
	for _ in range(8):
		print(cpu.load, cpu.temperature)
		sleep(1.1)
