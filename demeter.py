import os
import time
import platform

def Main():
	os.system('title Demeter: Operating System info on the go!')
	os.system('color a')
	print('Demeter Client \n')
	machine = platform.machine()
	version = platform.version()
	plform = platform.platform()
	system = platform.system()
	proc = platform.processor()
	
	print('Machine: ' + machine)
	print('Version: ' + version)
	print('Platform: ' + plform)
	print('System: ' + system)
	print('Processor: ' + proc + '\n')
	
	print('[!] Program Will Close After 3-4 minutes to save CPU power!')
	time.sleep(225)
	
if __name__ == '__main__':
	Main()