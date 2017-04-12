import socket, threading, sys

def wait_resp(conn):
	while True:
		resp = conn.recv(2048)
		if not resp:
			sys.exit()
		sys.stdout.write('\n{}'.format(resp.decode('utf-8')))
		sys.stdout.flush()

def send_cmds(conn):
	while True:
		cmd = sys.stdin.readline()
		conn.send('{}'.format(cmd).encode('utf-8'))

host, port = ('', 8888)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((host, port))
	sock.listen(5)
	print('Listener started at {}:{}\n'.format(host, port))
	conn, addr = sock.accept()
	print('conn ', addr)
	threads = [{'target': wait_resp, 'args': (conn,)}, {'target': send_cmds, 'args': (conn,)}]
	for thread in threads:
		threading.Thread(target=thread['target'], args=thread['args']).start()