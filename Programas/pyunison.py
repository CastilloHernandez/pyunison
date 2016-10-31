import ConfigParser
import os
import time
import sys 

cfg = ConfigParser.RawConfigParser()
cfg.optionxform = str
cfg.read('pyunison.ini')
for i,j in cfg.items('directorios'):
	sys.stdout.write('\x1b]2; Pyunison - ' + i + ' - ' + j + '\x07')
	print 'Pyunison - ' + i + ' - ' + j 
	print len('Pyunison - ' + i + ' - ' + j) * '=' 
	print
	os.system('unison ' + i + ' ' + j + '')
	print
sys.stdout.write("\x1b]2;Pyunison - Terminado\x07")
