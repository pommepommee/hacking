import sys
import socket
import numpy as np
import re

hostname = "109.232.232.225"
port = "15003"
datas = []

summ = []
results = []

def netcat(host, port, content=""):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, int(port)))
	s.send(content.encode())
	while True:
		data = s.recv(1048)
		if not data:
			break
		datas.append(data)
		if b"Resultat" in data:
			break
	print(datas)
		
	
netcat(hostname, port)


"""
hostname = "109.232.232.225"
port = "15003"
ans = ""
datas = []
summ = []
results = []

for line in fileinput.input():
	print(line, file=sys.stderr, flush=True)
	if "PASSWORD" in line:
		line = line.replace('[+]', '')
		line = re.sub("\*[A-Z ]*\[\s*\d+\]\s*(\+|\=)", "", line)
		line = line.split()
		line = list(map(int, line))
		#print(line, file=sys.stderr, flush=True)
		results.append(line.pop(-1))
		summ.append(line)
		
	elif "Resultat" in line:
		x = np.linalg.solve(summ, results)
		y = list(map(round, x))
		for el in y:
			ans += chr(el)
		print(ans)
		summ = []
		results = []
		ans = ""	
"""
